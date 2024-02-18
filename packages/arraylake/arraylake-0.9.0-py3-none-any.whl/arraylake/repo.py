"""
The Repo module contains the Arraylake classes for interacting with repositories, #AsyncRepo and #Repo.

The #Repo class provides a Zarr-compatible store interface for use with Zarr, Xarray, and other libraries
that support the Zarr protocol.

Repos should not be instantiated directly--instead, use the #Client and #AsyncClient, i.e.

```python
from arraylake import Client
client = Client()
repo = client.get_repo("my-org/my-repo")
```
"""

from __future__ import annotations

import asyncio
import datetime
import functools
import itertools
import json
import math
import os
import pathlib
import random
import re
import warnings
from collections import ChainMap
from collections.abc import AsyncGenerator, Awaitable, Mapping, MutableMapping, Sequence
from contextlib import contextmanager
from dataclasses import dataclass
from html import escape
from typing import TYPE_CHECKING, Any, Callable, Optional, TypeVar
from uuid import uuid4

import aioitertools as aioiter
import zarr
from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    TypeAdapter,
    field_serializer,
    field_validator,
)
from zarr._storage.store import StoreV3
from zarr.util import normalize_storage_path

import arraylake.retrier as retrier
from arraylake import config as config_obj
from arraylake.asyn import gather_with_throttled_concurrency, sync
from arraylake.chunkstore import Chunkstore
from arraylake.commits import CommitData, CommitLog
from arraylake.exceptions import (
    CommitFailedError,
    DocumentNotFoundError,
    InvalidPrefixError,
)
from arraylake.log_util import get_logger
from arraylake.metastore import MetastoreDatabase
from arraylake.types import (
    Author,
    BranchName,
    CollectionName,
    CommitID,
    CommitIDHex,
    DBIDBytes,
    NewCommit,
    NewSession,
    Path,
    ReferenceData,
    SessionExpirationUpdate,
    SessionID,
    SessionPathsResponse,
    SessionType,
    Tree,
    to_dbid_bytes,
)
from arraylake.virtual import (
    VirtualLocation,
    reformat_kerchunk_refs,
    scan_grib2,
    scan_netcdf,
    scan_tiff,
    scan_zarr_v2,
)
from arraylake.zarr_util import (
    DATA_ROOT,
    ENTRY_POINT_METADATA,
    META_ROOT,
    is_chunk_key,
    is_meta_key,
)

if TYPE_CHECKING:
    import xarray as xr

VIRTUAL_WARNING_MESSAGE = """
`path` cannot start with s3://. The syntax for `add_virtual_{format}` has changed
to mirror that of `cp source destination`.
The previous syntax was `add_virtual_{format}(destination, source).
Please rewrite to `add_virtual_{format}(destination, source) to silence this warning.
"""
THROTTLE_CONCURRENCY_SIZE = int(os.environ.get("ARRAYLAKE_THROTTLE_CONCURRENCY_SIZE", 4))

logger = get_logger(__name__)

metadata_collection = CollectionName("metadata")
chunks_collection = CollectionName("chunks")
nodes_collection = CollectionName("nodes")

DEFAULT_IS_WRITE_SESSION = True
DEFAULT_SESSION_TIMEOUT = datetime.timedelta(days=1)

RT = TypeVar("RT")

# Type adapters
LIST_OF_REFERENCEDATA_ADAPTER = TypeAdapter(list[ReferenceData])


def _write_op(func: Callable[..., RT]) -> Callable[..., RT]:
    """
    Decorator for write operations. Ensures that the repo is in a writable state.
    """

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.session.session_type == SessionType.write or self.session.branch is None:
            raise OSError("Repo is not writable. Try checking out the repository first using `repo.checkout(for_writing=True)`.")
        return func(self, *args, **kwargs)

    return wrapper


AsyncFunctionOrGenerator = TypeVar("AsyncFunctionOrGenerator", AsyncGenerator, Awaitable)


def _dispatch_over_collections(func: Callable[..., AsyncFunctionOrGenerator], prefix: str, **kwargs) -> list[AsyncFunctionOrGenerator]:
    """A utility function for calling async functions against multiple collections.

    Args:
        func: The function to call. It should accept `prefix` as the first argument and `collection` as a keyword argument.
        prefix: The prefix to use for the function call. If the prefix starts with `meta`.
            The function will be called against the metadata_collection. If the prefix starts with `data`,
            the function will be called against the chunks_collection. If the prefix is empty, the function
            will be called against both collections.
        kwargs: Keyword arguments to pass to the function

    Returns:
        A list of results from the function calls (length 0, 1, or 2). These can be awaited or async iterated over,
        depending on the input function return type.
    """

    collections = {"data": chunks_collection, "meta": metadata_collection}

    if prefix == "":
        return [func(prefix, collection=c, **kwargs) for c in collections.values()]

    key = prefix[:4]
    collection = collections.get(key)
    if collection:
        return [func(prefix, collection=collection, **kwargs)]
    else:
        raise InvalidPrefixError(f"Invalid prefix: {0}. Prefix should start with 'meta', 'data' or be the empty string.".format(prefix))


class LocalSession(BaseModel):
    id: SessionID = Field(alias="_id")
    db: MetastoreDatabase
    session_type: SessionType
    start_time: datetime.datetime

    # TODO: Enforce that BranchName cannot be None. Currently, some tests
    # require that it accept None as a valid type, since some tests require a
    # write session upon checkout() of a detached commit.
    #
    # We should update these tests and do proper enforcement here and in
    # create_session(), below.
    branch: Optional[BranchName] = None
    base_commit: Optional[CommitID] = None
    author_name: Optional[str] = None
    author_email: EmailStr

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @field_validator("base_commit", mode="before")
    @classmethod
    def validate_base_commit(cls, id: Any) -> Optional[DBIDBytes]:
        return to_dbid_bytes(id) if id is not None else None

    @field_serializer("base_commit")
    def serialize_base_commit(self, base_commit: Optional[CommitID]) -> Optional[CommitIDHex]:
        if base_commit is not None:
            return str(base_commit)
        else:
            return None


class LocalWriteSession(LocalSession):
    expiration: datetime.datetime
    message: Optional[str]

    async def update_expiration(self, expires_in: datetime.timedelta):
        server_session = await self.db.update_session_expiration(SessionExpirationUpdate(session_id=self.id, expires_in=expires_in))
        self.expiration = server_session.expiration

        return self

    async def abandon(self):
        server_session = await self.db.expire_session(session_id=self.id)
        self.expiration = server_session.expiration

        return self


class LocalReadSession(LocalSession):
    # TODO: Setup metadata caching post-init.
    pass


def as_write_session(local_session: LocalSession) -> LocalWriteSession:
    """This function is a pass-through type converter to appease mypy

    This performs type narrowing
    (https://mypy.readthedocs.io/en/stable/type_narrowing.html) to avoid mypy
    errors confusing a LocalWriteSession for an instance of the LocalSession
    base class."""
    if type(local_session) is LocalWriteSession:
        return local_session
    else:
        raise RuntimeError("Invalid session type. Attempting to perform a write operation with a read-only session.")


class AsyncRepo:
    """Asynchronous interface to Arraylake repo.

    :::note
    Because Zarr does not support asynchronous I/O, the async client cannot be used to read or write Zarr data directly.
    :::
    """

    db: MetastoreDatabase
    chunkstore: Chunkstore
    repo_name: str
    author: Author

    _db: MetastoreDatabase | None
    _commit_data: CommitData | None  # set in commit_data
    _writable: bool
    _prefetched_docs: MutableMapping[Path, Mapping[str, Any]]
    _prefetched_chunk_refs: MutableMapping[Path, ReferenceData]
    _session: LocalSession | None  # set in checkout

    def __init__(self, metastore_db: MetastoreDatabase, chunkstore: Chunkstore, name: str, author: Author):
        """
        Args:
            metastore_db: A metastore database for storing metadata
            chunkstore: A chunkstore for storing chunks
            name: The name of the repo. Purely for display purposes.
            author: The author name and email for commits
        """
        self.db = metastore_db
        self.chunkstore = chunkstore
        self.repo_name = name
        self.author = author

        # The following can't be initialized until we're in the async context because we need to query the metastore
        self._commit_data = None
        self._session = None
        self._writable = False
        self._prefetched_docs = {}
        self._prefetched_chunk_refs = {}

    def __getstate__(self):
        return self.db, self.chunkstore, self.repo_name, self.author, self._session

    def __setstate__(self, state):
        self.db, self.chunkstore, self.repo_name, self.author, self._session = state
        # commit_data can be large and is not needed for most operations, therefore we omit it during serialization.
        self._commit_data = None
        # Don't persist cache.
        self._prefetched_docs = {}
        self._prefetched_chunk_refs = {}

    def __repr__(self):
        repo_name = self.repo_name
        return f"<arraylake.repo.AsyncRepo name='{repo_name}'>"

    @property
    def session(self) -> LocalSession:
        # accessing the session via this property makes mypy happy
        if self._session is None:
            raise ValueError("There is no session active. You have to call checkout first.")
        return self._session

    async def commit_data(self, refresh: bool = False) -> CommitData:
        """Returns the #CommitData for the current session."""
        if refresh or self._commit_data is None:
            # refresh commit data
            commit_list, (tags, branches) = await asyncio.gather(self.db.get_commits(), self.db.get_refs())
            self._commit_data = CommitData(commit_list, tags, branches)

        return self._commit_data

    async def commit_log(self) -> CommitLog:
        """Returns the #CommitLog for the current session."""

        return CommitLog(self.repo_name, self.session.base_commit, await self.commit_data(True))

    async def status(self, limit: int = 1000) -> SessionStatus:
        """Returns the #SessionStatus for the current session.

        Args:
            limit (int): [Optional] The number of modified paths to return. Defaults to 1000, passing 0
            is equivalent to setting no limit.
        """
        modified_paths = {(spr.path, spr.deleted) async for spr in self._modified(limit=limit)}
        if len(modified_paths) >= limit:
            warnings.warn(
                f".status results were limited to the first {limit} records. If more records are required, use .status(limit={limit})"
            )
        return SessionStatus(repo_name=self.repo_name, session=self.session, modified_paths=list(modified_paths))

    async def ping(self) -> None:
        """Ping the metastore to confirm connection"""
        await self.db.ping()
        await self.chunkstore.ping()

    async def _get_ref_for_checkout(self, ref: str | CommitID):
        from .commits import get_ref

        if isinstance(ref, str):
            try:
                ref = CommitID.fromhex(ref)
            except ValueError:
                # Not a commit we will try branches and tags
                pass

        if isinstance(ref, DBIDBytes):
            commit_data = await self.commit_data()
            return get_ref(ref, commits=commit_data.commits, branches=commit_data.branches, tags=commit_data.tags)
        else:
            branches_list = await self.db.get_branches(names=[BranchName(ref)])
            branches = {branch.id: branch.commit_id for branch in branches_list}
            tag_list = await self.db.get_tags()
            tags = {tag.id: tag.commit_id for tag in tag_list}
            return get_ref(ref, branches=branches, tags=tags)

    async def create_session(
        self,
        ref: str | CommitID = "main",
        for_writing: bool = DEFAULT_IS_WRITE_SESSION,
        expires_in: datetime.timedelta = DEFAULT_SESSION_TIMEOUT,
        message: str | None = None,
    ) -> LocalSession:
        session_start_time = datetime.datetime.utcnow()

        # TODO: This is a temporary hack to allow our users to pass CommitIDs
        # instead of strings. We need to change the type annotation to match
        ref = str(ref) if isinstance(ref, DBIDBytes) else ref
        commit, branch = await self._get_ref_for_checkout(ref)

        session_type = SessionType.read_only

        if for_writing:
            session_type = SessionType.write

            if branch is None:
                # If it's not on the branch tip, we can't have a writable
                # session, so we create a read-only session.
                warnings.warn("You are not on a branch tip, so you can't commit changes.")

            if config_obj.config.get("server_managed_sessions", True):
                session_req = NewSession(
                    branch=branch,
                    base_commit=commit,
                    author_email=self.author.email,
                    author_name=self.author.name,
                    message=message,
                    session_type=session_type,
                    expires_in=expires_in,
                )
                server_session = await self.db.create_session(session_req)

                self._session = LocalWriteSession(_id=server_session.id, db=self.db, **server_session.model_dump())

            # TODO: Remove this once server-managed sessions are mandatory.
            else:
                expiration = session_start_time + expires_in
                self._session = LocalWriteSession(
                    _id=SessionID(uuid4().hex),
                    db=self.db,
                    branch=branch,
                    base_commit=commit,
                    session_type=session_type,
                    author_email=self.author.email,
                    author_name=self.author.name,
                    start_time=session_start_time,
                    expiration=expiration,
                    message=message,
                )
        else:
            self._session = LocalReadSession(
                _id=SessionID(f"read-{commit}"),
                db=self.db,
                branch=branch,
                base_commit=commit,
                session_type=session_type,
                author_email=self.author.email,
                author_name=self.author.name,
                start_time=session_start_time,
            )

        return self._session

    async def join_session(self, session_id: SessionID) -> LocalSession:
        if config_obj.config.get("server_managed_sessions", True):
            server_session = await self.db.get_session(session_id)
            self._session = LocalWriteSession(_id=server_session.id, db=self.db, **server_session.model_dump())
            return self._session
        else:
            raise ValueError("Joining sessions not supported. Enable the 'server_managed_sessions' config setting to access this feature.")

    # TODO: Remove the "| None" return type. Unfortunately, this is because
    # some checkouts in our test suite apparently can have None as a ref? We
    # should better document and guard against weird behavior like that.
    async def checkout(
        self,
        ref: str | CommitID = "main",
        session_token: SessionID | None = None,
        for_writing: bool = DEFAULT_IS_WRITE_SESSION,
        expires_in: datetime.timedelta = DEFAULT_SESSION_TIMEOUT,
    ) -> CommitID | None:
        """Checkout a ref (branch, tag, or commit ID) and initialize a new session.

        Args:
            ref: Commit, branch, or tag name

        Returns:
            commit: #CommitID
        """

        if session_token:
            self._session = await self.join_session(session_token)
        else:
            self._session = await self.create_session(ref=ref, for_writing=for_writing, expires_in=expires_in)

        return self.session.base_commit

    # FIXME: This should also be decorated with @_write_op, but that currently
    # breaks a lot of tests.
    async def commit(self, message: str, auto_ff: bool = True, checkout_for_writing: bool = DEFAULT_IS_WRITE_SESSION) -> CommitID | None:
        """Commit this session's changes and start a new session.

        Args:
            message: Commit message
            auto_ff: Whether to automatically fast-forward the repo and retry if the commit fails
            checkout_for_writing: Whether to checkout the ensuing commit in `for_writing` mode (default: True)

        Returns:
            new_commit: ID of new commit
        """
        # TODO: why don't we use auto_ff here???
        return await self._single_commit(message, checkout_for_writing=checkout_for_writing)

    async def _old_style_single_commit(
        self, message: str, attempt=0, checkout_for_writing: bool = DEFAULT_IS_WRITE_SESSION
    ) -> CommitID | None:
        """Old method, needed for tests than ensure compatibility with clients <= 0.7.6

        Delete this method once arraylake 0.7.6 is no longer supported
        """
        max_attempts = int(config_obj.config.get("max_commit_attempts", 50))
        max_jitter = 5  # seconds
        if self.session.branch is None:
            raise RuntimeError("You are not on a branch tip, so you can't commit changes.")

        # TODO: Remove this logic and simply pass the current session to
        # self.db.new_commit().
        commit_metadata = NewCommit(
            session_id=self.session.id,
            session_start_time=self.session.start_time,
            parent_commit=self.session.base_commit,
            commit_time=datetime.datetime.utcnow(),
            author_name=self.author.name,
            author_email=self.author.email,
            message=message,
        )

        # If server-managed sessions are enabled, the server will validate if
        # the commit can happen and return an error if not
        try:
            new_commit = await self.db.new_commit(commit_metadata)
        except ValueError as err:
            if str(err).startswith("No changes to commit"):
                warnings.warn(str(err))
                return self.session.base_commit
            else:
                raise err

        new_branch = (self.session.base_commit is None) or (not await self.db.get_branches([self.session.branch]))
        try:
            await self.db.update_branch(
                self.session.branch,
                session_id=self.session.id,
                base_commit=self.session.base_commit,
                new_commit=new_commit,
                new_branch=new_branch,
            )
        # TODO: fix metastore impl. inconsistency around error classes here
        except (ValueError, RuntimeError) as err:
            if not (str(err).startswith("Failed to update branch") or str(err).startswith("Cannot create branch")):
                raise
            else:
                if attempt < max_attempts:
                    await logger.ainfo(f"Encountered commit conflict {attempt}, retrying")
                    # add a small amount of jitter to avoid dos
                    delay = random.uniform(0, max_jitter)
                    await asyncio.sleep(delay)
                    await self._old_style_rebase(new_commit)
                    return await self._old_style_single_commit(message, attempt=attempt + 1, checkout_for_writing=checkout_for_writing)
                else:
                    raise CommitFailedError(f"Failed to update branch {self.session.branch} to point to commit {new_commit.hex()}")

        # reset session parameters
        #
        # NOTE: It's necessary to be this verbose, because otherwise mypy
        # complains.
        local_session = as_write_session(self.session)
        checked_out_commit = await self.checkout(
            self.session.branch, for_writing=checkout_for_writing, expires_in=local_session.expiration - self.session.start_time
        )
        if checked_out_commit != new_commit:
            warnings.warn(
                f""""Some other commit (id={checked_out_commit}) happened after yours (id={new_commit}). \
                We are checking out branch {self.session.branch} pointing to the latest commit available."""
            )

        # even if we checkout a different commit, we still return the commit we just created
        return new_commit

    async def _mk_commit_waits(self) -> retrier.Waits:
        """Define a series of wait times for the commit + rebase algorithm.

        We have configurable increasing waits, with a max number of attempts and jitter added to each wait.

        The relevant configuration variables are:
        - commit_max_attempts (or the deprecated but supported max_commit_attempts), default 30
        - commit_start_mean_sleep_seconds, default 3
        - commit_max_mean_sleep_seconds, default 30
        - commit_sleep_increase_seconds, default 5
        - commit_jitter_factor, default 0.5
        """
        # don't try more than max_attempts times
        max_attempts = int(config_obj.config.get("max_commit_attempts", config_obj.config.get("commit_max_attempts", 30)))
        # never sleep more than max_wait
        max_wait = datetime.timedelta(seconds=int(config_obj.config.get("commit_max_mean_sleep_seconds", 30)))
        # start sleeping this much
        start_wait = datetime.timedelta(seconds=int(config_obj.config.get("commit_start_mean_sleep_seconds", 3)))

        # each retry increases mean wait time by wait_increase
        wait_increase_sec = float(config_obj.config.get("commit_sleep_increase_seconds", 5))
        if wait_increase_sec < 0:
            await logger.awarn(f"Ignoring commit_sleep_increase_seconds setting of {wait_increase_sec}, using 5 instead")
            wait_increase_sec = 5
        wait_increase = datetime.timedelta(seconds=wait_increase_sec)

        # each wait is jittered +- this factor
        jitter_factor = float(config_obj.config.get("commit_jitter_factor", 0.5))
        if not 0 < jitter_factor <= 1:
            await logger.awarn(f"Ignoring commit_jitter_factor setting of {jitter_factor}, using 0.5 instead")
            jitter_factor = 0.5

        linear_waits = retrier.linear_wait(delta=wait_increase, initial=start_wait)
        saturated_waits = map(lambda t: t if t <= max_wait else max_wait, linear_waits)
        # we jitter after saturating to maintain randomness
        jittered = retrier.proportional_jitter(factor=jitter_factor, waits=saturated_waits)
        # we add some brief waits to handle simple conflicts
        quick_waits = retrier.max_tries(
            2,
            retrier.linear_wait(
                delta=datetime.timedelta(seconds=1), initial=datetime.timedelta(seconds=min(1, start_wait.total_seconds()))
            ),
        )
        # we want the first attempt and the first retry to not wait,
        # a different writer could have committed a long time ago
        initial_waits = [datetime.timedelta()] * 2
        all = itertools.chain(initial_waits, quick_waits, jittered)
        limit_attempts = retrier.max_tries(max_attempts, all)
        return limit_attempts

    async def _single_commit(self, message: str, checkout_for_writing: bool) -> CommitID | None:
        """Create a new commit based on current state and attempt to write to branch.

        Returns `None` if there are no changes to commit
        """

        class Retry(Exception):
            pass

        session_branch = self.session.branch
        if session_branch is None:
            raise RuntimeError("You are not on a branch tip, so you can't commit changes.")

        session_id = self.session.id

        async def initial_attempt():
            # Do we have a chance of successfully committing?
            # If we don't "own" the tip of the branch we know updating the branch is going to fail,
            # so we don't even try, we sleep a bit and try a rebase
            existing_branch = next(iter(await self.db.get_branches([session_branch])), None)
            if existing_branch is not None and existing_branch.commit_id != self.session.base_commit:
                await logger.adebug("Tip of the branch is not the same as base commit")
                raise Retry("Tip of the branch is not the same as base commit")

            # At this point we think we are ready to commit, either:
            # - we are committing to a new branch
            # - or our base_commit is the tip of the existing branch
            #
            # The branch update can still fail though, maybe some other writer
            # created the branch or committed to it since the last time we checked.

            commit_metadata = NewCommit(
                session_id=session_id,
                session_start_time=self.session.start_time,
                parent_commit=self.session.base_commit,
                commit_time=datetime.datetime.utcnow(),
                author_name=self.author.name,
                author_email=self.author.email,
                message=message,
            )

            # If server-managed sessions are enabled, the server will validate if
            # the commit can happen and return an error if not
            try:
                new_commit = await self.db.new_commit(commit_metadata)
            except ValueError as err:
                if str(err).startswith("No changes to commit"):
                    warnings.warn(str(err))
                    return self.session.base_commit
                else:
                    raise err

            # TODO: Add a "has_branch" route?
            new_branch = self.session.base_commit is None or existing_branch is None
            try:
                await self.db.update_branch(
                    session_branch,
                    session_id=self.session.id,
                    base_commit=self.session.base_commit,
                    new_commit=new_commit,
                    new_branch=new_branch,
                )
            # TODO: fix metastore impl. inconsistency around error classes here
            except (ValueError, RuntimeError) as err:
                if not (str(err).startswith("Failed to update branch") or str(err).startswith("Cannot create branch")):
                    raise
                else:
                    await logger.adebug("Race condition updating branch, retrying")
                    raise Retry("Tip of the branch is not the same as base commit")

            # reset session parameters
            #
            # NOTE: It's necessary to be this verbose, because otherwise mypy
            # complains.
            local_session = as_write_session(self.session)
            checked_out_commit = await self.checkout(
                session_branch, for_writing=checkout_for_writing, expires_in=local_session.expiration - self.session.start_time
            )
            if checked_out_commit != new_commit:
                warnings.warn(
                    f""""Some other commit (id={checked_out_commit}) happened after yours (id={new_commit}). \
                    We are checking out branch {self.session.branch} pointing to the latest commit available."""
                )

            # even if we checkout a different commit, we still return the commit we just created
            return new_commit

        async def retried_attempt(_: Exception):
            await logger.ainfo("Encountered commit conflict, retrying")
            await self._rebase(base_commit=self.session.base_commit, session_id=session_id)
            return await initial_attempt()

        retry = retrier.Retrier.from_initial_and_retry(initial_attempt, retried_attempt).retry_on_exception_type(Retry)

        try:
            return await retry(await self._mk_commit_waits())
        except retrier.NoMoreRetriesError:
            raise CommitFailedError(f"Failed to update branch {session_branch}")

    async def _rebase(self, base_commit: CommitID | None, session_id: SessionID):
        """Update the session base commit to branch HEAD, if possible."""
        branch = self.session.branch
        if branch is None:
            raise ValueError("Session has no branch")
        try:
            latest_branch_commit_id = await self.db.rebase(base_commit=base_commit, session_id=session_id, upstream_branch=branch)
            self.session.base_commit = latest_branch_commit_id
            # FIXME: Call session.update()? Make a new session?
            self.session.base_commit = latest_branch_commit_id
        except ValueError as err:
            if not str(err).startswith("Branch does not exist"):
                raise

    async def _old_style_rebase(self, commit_id: CommitID):
        """Old method, needed for tests than ensure compatibility with clients <= 0.7.6

        Delete this method once arraylake 0.7.6 is no longer supported
        """
        branch = self.session.branch
        if branch is None:
            raise ValueError("Session has no branch")
        try:
            latest_branch_commit_id = await self.db.old_style_rebase(commit_id, branch)
            self.session.base_commit = latest_branch_commit_id
            await self.commit_data(refresh=True)
        except ValueError as err:
            if not str(err).startswith("Branch does not exist"):
                raise

    async def fast_forward(self):
        """Fast-forward the session.
        Attempts to update the session base commit to the latest branch tip.
        Will fail if the same paths have been modified in the current session and on the branch.
        """
        try:
            latest_commit = await self._try_fast_forward()
            # it succeeded; we can move the branch tip
            # FIXME: Call session.update()? Make a new session?
            self.session.base_commit = latest_commit
        except Exception:
            raise

    async def _try_fast_forward(self) -> CommitID | None:
        # returns the ID to ff to

        if self.session.branch is None:
            raise RuntimeError("Fast-forward unavailable: You are not on a branch tip")

        branch = self.session.branch
        maybe_matching_branch = await self.db.get_branches([branch])
        branch_latest_commit = maybe_matching_branch[0].commit_id if maybe_matching_branch else None
        session_base_commit = self.session.base_commit

        if branch_latest_commit is None:
            # that branch has seen no commits yet
            return branch_latest_commit

        if branch_latest_commit == session_base_commit:
            # no new commits have come in on this branch, nothing to ff
            return branch_latest_commit

        # our _modified check is unlimited
        # this is to ensure that any overlaps are accounted for when comparing to the modified
        # paths of other sessions later in the logic of fast forwarding
        modified_paths = {spr.path async for spr in self._modified(limit=0)}
        if len(modified_paths) == 0:
            # nothing changed; nothing to do
            return branch_latest_commit

        # this is different from self.commit_log because it starts from branch_latest_commit
        commit_log = CommitLog(self.repo_name, branch_latest_commit, await self.commit_data())
        upstream_modifications = set()
        for commit in commit_log:
            if commit.id == session_base_commit:
                # we can stop iterating
                break
            for collection in (metadata_collection, chunks_collection):
                upstream_modifications.update(
                    {
                        response.path
                        async for response in self.db.get_all_paths_for_session(
                            session_id=commit.session_id, base_commit=session_base_commit, collection=collection
                        )
                    }
                )
        conflicting_paths = upstream_modifications & modified_paths
        if conflicting_paths:
            raise RuntimeError(f"Can't fast-forward due to conflicting paths {conflicting_paths}.")
        return branch_latest_commit

    @_write_op
    async def _rename(self, src_path: Path, dst_path: Path) -> None:
        session = self.session
        await self.db.rename(src_path, dst_path, session_id=session.id, base_commit=session.base_commit)

    async def new_branch(self, branch_name: str) -> None:
        """Create a new branch based on the current session reference

        Args:
            branch_name: New branch name
        """

        branch = BranchName(branch_name)
        if self._session is None:
            # this was added to make mypy happy but is not covered by tests
            raise ValueError("There is no session active. You have to call checkout first.")
        if branch == self.session.branch or (await self.db.get_branches([branch])):
            raise ValueError(f"Branch {branch} already exists.")
        self._session.branch = branch

    @_write_op
    async def _set_doc(self, path: Path, *, content: dict) -> None:
        """Write a single document to the metastore

        Parameters
        ----------
        path : str
            Path to document in the metastore
        content : dict
            Document contents
        """
        await self._set_docs({path: content})

    @_write_op
    async def _set_docs(self, items: Mapping[Path, dict]) -> None:
        """Write multiple documents to the metastore

        Parameters
        ----------
        items : dict
            Mapping where the keys are document paths and values are documents in the form of dictionaries.
        """
        await self.db.add_docs(items, collection=metadata_collection, session_id=self.session.id, base_commit=self.session.base_commit)

    async def _get_doc(self, path: Path) -> Mapping[Path, Mapping[str, Any]]:
        """Get a single document from the metastore

        Parameters
        ----------
        path : str
            Path to document in the metastore

        Returns
        -------
        content : dict
            Document contents
        """
        if self._prefetched_docs:
            if path in self._prefetched_docs:
                logger.debug("__getitem__ prefetch hit:", path=path)
                return self._prefetched_docs[path]
            else:
                logger.debug("__getitem__ prefetch miss: ", path=path)

        result = await self._get_docs([path])
        try:
            return result[path]
        except KeyError:
            raise DocumentNotFoundError

    async def _doc_exists(self, path: Path) -> bool:
        """Check if a doc exists in the metastore

        Parameters
        ----------
        path : str
            Document path
        """
        if self._prefetched_docs:
            if path in self._prefetched_docs:
                logger.debug("_doc_exists, hit", path=path)
                return True
            else:
                logger.debug("_doc_exists, miss", path=path)

        try:
            # Here we are trading a small amount of extra data transfer
            # (just getting the whole doc) in order to simplify our code.
            # Since individual docs are all tiny, in practice, this should not have
            # any performance consequence, as other sources of latency are much, much higher.
            await self._get_doc(path)
            return True
        except DocumentNotFoundError:
            return False

    async def _get_docs(self, paths: Sequence[str]) -> Mapping[Path, Mapping[str, Any]]:
        """Get multiple documents from the metastore

        Parameters
        ----------
        paths : sequence of str
            Sequence of document paths

        Returns
        -------
        docs : dict
            Mapping where keys are document paths and values are documents in the form of dictionaries.
        """
        # Here we do what fsspec does and just OMIT the missing paths from the dictionary
        db_results = {}

        async for doc in self.db.get_docs(
            paths, collection=metadata_collection, session_id=self.session.id, base_commit=self.session.base_commit
        ):
            # TODO: this check is probably not necessary but needed to make mypy happy
            # error: Argument after ** must be a mapping, not "Optional[Dict[Any, Any]]"  [arg-type]
            if doc.content is not None:
                db_results[doc.path] = doc.content
        return db_results

    @_write_op
    async def _del_docs(self, paths: Sequence[str]) -> None:
        """Delete multiple documents from the metastore

        Parameters
        ----------
        paths : sequence of str
            Sequence of document paths
        """
        await self.db.del_docs(paths, collection=metadata_collection, session_id=self.session.id, base_commit=self.session.base_commit)

    @_write_op
    async def _del_doc(self, path: Path) -> None:
        """Delete a single documents from the metastore

        Parameters
        ----------
        path : str
            Document path
        """
        # make sure there is actually a doc there first
        # TODO: make this as inexpensive as possible
        _ = await self._get_doc(path)
        await self.db.del_docs([path], collection=metadata_collection, session_id=self.session.id, base_commit=self.session.base_commit)

    @_write_op
    async def _del_prefix(self, prefix: Path) -> None:
        """Delete all documents with a given prefix from the metastore

        Parameters
        ----------
        prefix : str
            Document path prefix
        """
        try:
            delete_functions = _dispatch_over_collections(
                self.db.del_prefix, prefix, base_commit=self.session.base_commit, session_id=self.session.id
            )
        except InvalidPrefixError:
            return
        await asyncio.gather(*delete_functions)

    @_write_op
    async def _set_chunk(self, path: Path, *, data: bytes) -> None:
        """Write a single chunk to the chunkstore and record it in the metastore's chunk manifest

        Parameters
        ----------
        path : str
            Document path
        data : bytes
            Chunk data
        """
        await self._set_chunks({path: data})

    @_write_op
    async def _set_chunks(self, items: Mapping[Path, bytes]) -> None:
        """Write a batch of chunks to the chunkstore and record them in the metastore's chunk manifest

        Parameters
        ----------
        path : str
            Document path
        data : bytes
            Chunk data
        """
        chunk_refs = await asyncio.gather(*(self.chunkstore.add_chunk(data, session_id=self.session.id) for data in items.values()))
        chunk_ref_dicts = LIST_OF_REFERENCEDATA_ADAPTER.dump_python(chunk_refs)
        await self.db.add_docs(
            dict(zip(items, chunk_ref_dicts)),
            collection=chunks_collection,
            session_id=self.session.id,
            base_commit=self.session.base_commit,
        )

    @_write_op
    async def _set_chunk_ref(self, path: Path, *, reference_data: ReferenceData) -> None:
        """Set a chunk reference in the metastore

        Parameters
        ----------
        path : str
            Document path
        reference_data : ReferenceData
            Chunk reference document
        """
        await self.db.add_docs(
            {path: reference_data.model_dump()},
            collection=chunks_collection,
            session_id=self.session.id,
            base_commit=self.session.base_commit,
        )

    @_write_op
    async def _set_chunk_refs(self, items: Mapping[Path, ReferenceData]) -> None:
        """Set multiple chunk reference documents in the metastore

        Parameters
        ----------
        items : dict
            Mapping where keys are paths and values are chunk reference documents in the form of dictionaries
        """
        chunk_refs = {k: ref.model_dump() for k, ref in items.items()}  # convert from pydantic model
        await self.db.add_docs(chunk_refs, collection=chunks_collection, session_id=self.session.id, base_commit=self.session.base_commit)

    async def _get_chunk_ref(self, path: Path) -> ReferenceData:
        """Get a single chunk reference from the metastore

        Parameters
        ----------
        path : str
            Document path

        Returns
        -------
        refdata : ReferenceData
            Chunk reference document
        """

        if path in self._prefetched_chunk_refs:
            logger.debug("_get_chunk_ref prefetch hit", path=path)
            return self._prefetched_chunk_refs[path]
        else:
            logger.debug("_get_chunk_ref prefetch miss", path=path)

        results = await self._get_chunk_refs([path])
        try:
            return results[path]
        except KeyError:
            raise DocumentNotFoundError

    async def _get_chunk_refs(self, paths: Sequence[str]) -> Mapping[Path, ReferenceData]:
        """Get multiple chunk references from the metastore

        Parameters
        ----------
        paths : sequence of str
            Sequence of document paths

        Returns
        -------
        docs : dict
            Mapping where keys are paths and values are chunk ``ReferenceData`` objects.
        """
        # Here we do what fsspec does and just OMIT the missing paths from the dictionary
        db_results = {}
        async for doc in self.db.get_docs(
            paths, collection=chunks_collection, session_id=self.session.id, base_commit=self.session.base_commit
        ):
            # TODO: this check is probably not necessary but needed to make mypy happy
            # error: Argument after ** must be a mapping, not "Optional[Dict[Any, Any]]"  [arg-type]
            if doc.content is not None:
                db_results[doc.path] = ReferenceData(**doc.content)

        return db_results

    async def _get_chunk(self, path: Path, *, validate: bool = False) -> bytes:
        """Get a chunk from the chunkstore

        Parameters
        ----------
        path : str
            Chunk path
        validate : bool, default=False
            If True, validate the chunk hash after retrieving it from the chunkstore
        """
        chunk_ref = await self._get_chunk_ref(path)
        chunk = await self.chunkstore.get_chunk(chunk_ref, validate=validate)
        return chunk

    async def _get_chunks(self, paths: Sequence[Path]) -> Mapping[Path, bytes]:
        """Get multiple chunks from the chunkstore

        Parameters
        ----------
        paths : sequence of str
            Sequence of chunk paths

        Returns
        -------
        chunks : dict
            Mapping where keys are paths and values are chunk objects in the form of bytes.
        """
        chunk_refs = await self._get_chunk_refs(paths)

        # TODO: there is a scenario that presents a race condition here:
        # - chunk_refs are fetched
        # - chunk manifest deduplication process runs
        # - GC runs deleting some of the chunk_refs keys in object store
        # - The chunkstore cannot find those keys
        # - A simple solution is to detect that keys are not found and retry the
        #   _get_chunk_refs operation
        # - This can be done for eiter the failing key only, or all keys, or a
        #   something in between those options.

        chunks = await asyncio.gather(*(self.chunkstore.get_chunk(ref) for ref in chunk_refs.values()))
        return dict(zip(chunk_refs, chunks))

    async def _chunk_exists(self, path: Path) -> bool:
        """Check if a chunk exists in the metastore

        Parameters
        ----------
        path : str
            Chunk path

        Returns
        -------
        bool

        .. note:: The presence of the chunk is only checked in the metastore's chunk manifest, not the chunkstore.
        """
        try:
            await self._get_chunk_ref(path)
            return True
        except DocumentNotFoundError:
            return False

    @_write_op
    async def _del_chunk(self, path: Path) -> None:
        """Delete a single chunk from the metastore

        Parameters
        ----------
        path : str
            Document path

        .. note:: This method does not remove the chunk from the chunkstore, only the metastore's chunk manifest

        """
        _ = await self._get_chunk_ref(path)
        await self.db.del_docs([path], collection=chunks_collection, session_id=self.session.id, base_commit=self.session.base_commit)

    @_write_op
    async def _del_chunks(self, paths: Sequence[str]) -> None:
        """Delete multiple chunks from the metastore

        Parameters
        ----------
        paths : sequence of str
            Sequence of chunk paths

        .. note:: This method does not remove chunks from the chunkstore, only the metastore's chunk manifest
        """
        await self.db.del_docs(paths, collection=chunks_collection, session_id=self.session.id, base_commit=self.session.base_commit)

    # Note: this implementation does not support implicit groups!
    # The zarr V3 abstract store interface (https://zarr-specs.readthedocs.io/en/latest/core/v3.0.html#abstract-store-interface) says
    # > For example, if a store contains the keys “a/b”, “a/c”, “a/d/e”, “a/f/g”
    # > then _list_dir("a/") would return keys “a/b” and “a/c” and prefixes “a/d/” and “a/f/”.
    # > _list_dir("b/") would return the empty set.
    # This is problematic for us for because, even if we could discover the prefixes "a/d/" and "a/f/", we couldn't
    # assign a unique session_id to them.
    # To resolve this, I propose we DISALLOW IMPLICIT GROUPS. This will help a lot, because every "directory"
    # corresponds to a .group.json document.

    async def _list(self, prefix: str, *, all_subdirs: bool = False, filter: str | None = None) -> AsyncGenerator[Path, None]:
        """Convenience function to dispatch queries to the right collection"""
        kwargs = dict(
            session_id=self.session.id,
            base_commit=self.session.base_commit,
            all_subdirs=all_subdirs,
            filter=filter,
        )
        try:
            async_generators = _dispatch_over_collections(self.db.list, prefix, **kwargs)
        except InvalidPrefixError:
            return
        for agen in async_generators:
            async for path in agen:
                yield path

    async def _list_dir(self, prefix: str) -> AsyncGenerator[Path, None]:
        """List a directory in the metastore

        Parameters
        ----------
        prefix : str

        Yields
        ------
        path : str
            Document path
        """
        path_query = normalize_storage_path(prefix)

        # TODO: refactor all of this once Zarr python reverts to not having a top-level entry point
        # we don't need a query for these; they are guaranteed to exist
        if path_query == "":
            for prefix in ["data", "meta", "zarr.json"]:
                yield prefix
            return
        elif path_query == "data":
            yield "root"
            return

        start = len(path_query) + 1
        groups_seen = set()
        async for path in self._list(path_query, all_subdirs=False):
            # a group may end with .group.json (explicit) or have no
            # suffix (implicit). in the group
            # (in progress) should this logic be tweaked to find items without a suffix too (i.e a dir?)
            if path.endswith(".group.json"):
                p = path[start:-11]
                if p not in groups_seen:
                    yield path[start:]
                    groups_seen.add(p)
            else:
                # trim the start of the path off, we only want what's in the dir
                # e.g. meta/root/baz.array.json -> baz.array.json
                yield path[start:]

    async def _list_prefix(self, prefix: str) -> AsyncGenerator[str, None]:
        """List a prefix in the metastore

        Parameters
        ----------
        prefix : str

        Yields
        ------
        path : str
            Document path
        """

        # starting with a prefix is invalid
        if prefix.startswith("/"):
            raise ValueError("prefix must not begin with /")
        path_query = normalize_storage_path(prefix)

        # The function normalize_storage_path is responsible for cleaning paths,
        # which includes removing leading and trailing slashes ("/"). However,
        # if the provided prefix already has a trailing slash, it should be retained.
        # This is important because store.list_dir uses store.list_prefix,
        # but list_dir only supports directory listing and not general
        # key prefix matching. To ensure proper functionality, we need to make
        # sure that the prefix we use includes a trailing slash in this case.
        if prefix.endswith("/"):
            path_query += "/"

        async for path in self._list(path_query, all_subdirs=True):
            yield path
        if path_query == "":
            yield "zarr.json"

    async def _modified(self, limit=1000) -> AsyncGenerator[SessionPathsResponse, None]:
        """Get modified paths for session, across both chunks, metadata and nodes.

        We query multiple collections to determine modified paths. To enforce a limit, we manually
        manage the number of docs that we yield with this call.

        Nodes will be represented with their path.
        """
        iter = functools.partial(
            self.db.get_all_paths_for_session, session_id=self.session.id, base_commit=self.session.base_commit, limit=limit
        )
        all = aioiter.chain(iter(collection=nodes_collection), iter(collection=metadata_collection), iter(collection=chunks_collection))

        # we need to convert 0 to None
        slice_limit = limit if limit else None
        async for res in aioiter.islice(all, slice_limit):
            yield res

    async def _getsize(self, prefix: str) -> int:
        """Get the size of a prefix in the metastore

        Parameters
        ----------
        prefix : str

        Returns
        -------
        size : int
            Size of all documents in the prefix (only includes chunks, not metadata)
        """
        path_query = normalize_storage_path(prefix)
        response = await self.db.getsize(
            path_query,
            session_id=self.session.id,
            base_commit=self.session.base_commit,
        )
        return response.total_chunk_bytes

    async def _tree(self, prefix: str = "", depth: int = 10, filter: str | None = None) -> Tree:
        """Display this repo's hierarchy as a Rich Tree

        Args:
            prefix: Path prefix
            depth: Maximum depth to descend into the hierarchy
            filter: Optional JMESPath query to filter by
        """

        # this is a bit fragile but will go away soon
        if not prefix.startswith("meta/"):
            prefix = "meta/" + prefix

        tree_obj = await self.db.tree(
            prefix=prefix,
            depth=depth,
            session_id=self.session.id,
            base_commit=self.session.base_commit,
            filter=filter,
        )
        return tree_obj

    async def tree(self, prefix: str = "", *, depth: int = 10, filter: str | None = None) -> Tree:
        """Display this repo's hierarchy as a Rich Tree

        Args:
            prefix: Path prefix
            depth: Maximum depth to descend into the hierarchy
            filter: Optional JMESPath query to filter by
        """
        return await self._tree(prefix, depth, filter=filter)

    async def _prefetch_docs(self, paths: Sequence[str]) -> None:
        try:
            self._prefetched_docs.update(await self._get_docs(paths))
        except DocumentNotFoundError as e:
            logger.debug("failed to prefetch.", paths=paths, error=str(e))
            return

    async def _prefetch_coordinate_chunk_refs(self) -> None:
        # cache dimension coordinate chunks.
        # This is a list of list of chunk paths per variable/node
        # The inner lists get passed to _get_chunks
        chunks_to_request: list[list[Path]] = []
        for path, value in self._prefetched_docs.items():
            if "array.json" in path:
                varname = pathlib.Path(path).name.replace(".array.json", "")
                # Check that this is a 1D array where the array name matches the
                # dimension name. Xarray uses this heuristic to load the array
                # into memory when creating datasets. We cache chunk refs for such
                # variables.
                if value["attributes"].get("_ARRAY_DIMENSIONS", None) == [varname]:
                    chunk_shape = value["chunk_grid"]["chunk_shape"]
                    (chunklen,) = chunk_shape
                    (numel,) = value["shape"]
                    nchunks = int(math.ceil(numel / chunklen))
                    newpath = path.replace("meta", "data").replace(".array.json", "")
                    # append a list of chunk paths per variable to pass to _get_chunk_refs
                    chunks_to_request.append([Path(f"{newpath}/c{i}") for i in range(nchunks)])

        chunk_refs: list[Mapping[Path, ReferenceData]] = await gather_with_throttled_concurrency(
            THROTTLE_CONCURRENCY_SIZE,
            *(self._get_chunk_refs(batch) for batch in chunks_to_request),
        )
        # Argument 1 to "ChainMap" has incompatible type "*list[Mapping[str, bytes]]"; expected "MutableMapping[Never, Never]"
        self._prefetched_chunk_refs.update(ChainMap(*chunk_refs))  # type: ignore[arg-type]

    def _chunk_locations_to_refs(self, locations: dict[Path, VirtualLocation]) -> dict[Path, ReferenceData]:
        return {
            path: ReferenceData.new_virtual(
                for_version=self.chunkstore.write_schema_version, uri=loc.uri, offset=loc.offset, length=loc.length, sid=self.session.id
            )
            for path, loc in locations.items()
        }

    @_write_op
    async def add_virtual_grib(self, grib_uri: str, path: Path, **kwargs) -> None:
        """Add a virtual GRIB2 dataset to the repo.

        If the GRIB file contains multiple messages, this method will attempt to
        concatentate the messages to a single Zarr store, where the data payload
        of each message in a single chunk.

        Warning: This method has only been tested with a limited number of GRIB2
        files. Please file an issue for GRIB2 files that don't work as expected.

        Args:
            grib_uri: The path to the GRIB2 file. Only `s3://` URIs are supported at the moment.
            path: The path within the repo where the virtual dataset should be created.
            kwargs: Additional arguments to pass to the kerchunk
              [file format backend](https://fsspec.github.io/kerchunk/reference.html#file-format-backends).
              Do not pass `storage_options` or `inline_threshold`.
        """
        kerchunk_refs = scan_grib2(grib_uri, **kwargs)
        meta_docs, chunk_locations, inlined_refs = reformat_kerchunk_refs(kerchunk_refs, path)
        await self._set_docs(meta_docs)
        await self._set_chunk_refs(self._chunk_locations_to_refs(chunk_locations))
        await self._set_chunks(inlined_refs)

    @_write_op
    async def add_virtual_netcdf(self, netcdf_uri: str, path: Path, **kwargs) -> None:
        """Add a virtual Netcdf dataset to the repo.

        Args:
            netcdf_uri: The path to the netCDF file. Only `s3://` URIs are supported at the moment.
              Both netCDF4 and netCDF3 files are supported.
            path: The path within the repo where the virtual dataset should be created.
            kwargs: Additional arguments to pass to the kerchunk
              [file format backend](https://fsspec.github.io/kerchunk/reference.html#file-format-backends).
              Do not pass `storage_options` or `inline_threshold`.
        """
        if path.startswith("s3://"):
            warnings.warn(VIRTUAL_WARNING_MESSAGE.format(format="netcdf"), FutureWarning)
            path, netcdf_uri = netcdf_uri, path
        kerchunk_refs = scan_netcdf(netcdf_uri, **kwargs)
        meta_docs, chunk_locations, inlined_refs = reformat_kerchunk_refs(kerchunk_refs, path)
        if inlined_refs:
            raise ValueError("Inlined references are not supported by Arraylake.")
        await self._set_docs(meta_docs)
        await self._set_chunk_refs(self._chunk_locations_to_refs(chunk_locations))

    @_write_op
    async def add_virtual_zarr(self, zarr_uri: str, path: Path) -> None:
        """Add a virtual Zarr dataset to the repo.

        Args:
            zarr_uri: The path to the Zarr store. Only Zarr V2 stores and `s3://` URIs are supported at the moment.
            path: The path within the repo where the virtual dataset should be created.
        """
        if path.startswith("s3://"):
            warnings.warn(VIRTUAL_WARNING_MESSAGE.format(format="zarr"), FutureWarning)
            path, zarr_uri = zarr_uri, path
        kerchunk_refs = scan_zarr_v2(zarr_uri)
        meta_docs, chunk_locations, inlined_refs = reformat_kerchunk_refs(kerchunk_refs, path)
        if inlined_refs:
            raise ValueError("Inlined references are not supported by Arraylake.")
        await self._set_docs(meta_docs)
        await self._set_chunk_refs(self._chunk_locations_to_refs(chunk_locations))

    @_write_op
    async def add_virtual_tiff(self, tiff_uri: str, path: Path, name: str, **kwargs) -> None:
        """Add a virtual TIFF dataset to the repo.
        Args:
            tiff_uri: The path to the TIFF file. Only `s3://` URIs are supported at the moment.
            path: The path within the repo where the virtual dataset should be created.
                Unlike the other virtual functions, this path should include the array name.
            name: TIFF files contian bare arrays without a name. You must provide one.
            kwargs: Additional arguments to pass to the kerchunk
                [file format backend](https://fsspec.github.io/kerchunk/reference.html#file-format-backends).
                Do not pass `storage_options` or `inline_threshold`.

        Notes:
            Arrays will be ingested with dimension names 'X', 'Y'[, 'band']
            TIFFs with overviews will be ingested so that there is one array
            per overview level named '0', '1', '2', etc.
        """
        kerchunk_refs = scan_tiff(tiff_uri, name, **kwargs)
        meta_docs, chunk_locations, inlined_refs = reformat_kerchunk_refs(kerchunk_refs, path)
        if inlined_refs:
            raise ValueError("Inlined references are not supported by Arraylake.")
        await self._set_docs(meta_docs)
        await self._set_chunk_refs(self._chunk_locations_to_refs(chunk_locations))

    async def filter_metadata(self, filter: str) -> list[str]:
        """
        Filter repo metadata documents using a JMSE search string.

        https://jmespath.org/specification.html
        """
        items = self._list(META_ROOT, all_subdirs=True, filter=filter)
        results = []
        async for result in items:
            matches = re.match(rf"{META_ROOT}(.*)(\.array|\.group).json", result)
            if matches:
                results.append(matches.group(1))
        return results


def _sort_keys(keys: Sequence[str]) -> tuple[list[str], list[str]]:
    """Convenience function to sort keys into meta_keys and chunk_keys"""
    chunk_keys = []
    meta_keys = []
    bad_keys = []
    for key in keys:
        if is_chunk_key(key):
            chunk_keys.append(key)
        elif is_meta_key(key):
            meta_keys.append(key)
        else:  # pragma: no cover
            bad_keys.append(key)
    if bad_keys:  # pragma: no cover
        # don't expect to get here because we have already called self._validate_key
        raise ValueError(f"unexpected keys: {key}")
    return meta_keys, chunk_keys


class Repo:
    """Synchronous interface to Arraylake repo."""

    _arepo: AsyncRepo
    _OPEN: bool

    def __init__(self, arepo: AsyncRepo):
        """
        Initialize a Repo from an initialized AsyncRepo

        Args:
            arepo: An existing AsyncRepo
        """
        self._arepo = arepo

    @classmethod
    def from_metastore_and_chunkstore(cls, metastore_db: MetastoreDatabase, chunkstore: Chunkstore, name: str, author: Author) -> Repo:
        """
        Initialize a Repo from an initialized metastore database and chunkstore

        Args:
            metastore_db: A metastore database for storing metadata
            chunkstore: A chunkstore for storing chunks
            name: The name of the repo. Purely for display purposes.
            author: The author name and email for commits
        """
        arepo = AsyncRepo(metastore_db, chunkstore, name, author)
        repo = cls(arepo)
        repo.checkout()
        return repo

    @property
    def repo_name(self) -> str:
        return self._arepo.repo_name

    def close(self):
        warnings.warn("Closing repo no longer required.", DeprecationWarning)

    def _synchronize(self, method, *args, **kwargs):
        @functools.wraps(method)
        def wrap(*args, **kwargs):
            return sync(method, *args, **kwargs)

        return wrap(*args, **kwargs)

    def _wrap_async_iter(self, func, *args, **kwargs):
        async def iter_to_list():
            # TODO: replace with generators so we don't load massive lists into memory
            # (e.g. list_prefix(""))
            return [item async for item in func(*args, **kwargs)]

        return self._synchronize(iter_to_list)

    def __getstate__(self):
        return self._arepo

    def __setstate__(self, state):
        self._arepo = state

    def __repr__(self):
        repo_name = self._arepo.repo_name
        return f"<arraylake.repo.Repo '{repo_name}'>"

    def ping(self):
        """Ping the metastore to confirm connection"""

        return self._synchronize(self._arepo.ping)

    def checkout(
        self,
        ref: str | CommitID = "main",
        session_token: SessionID | None = None,
        for_writing: bool = DEFAULT_IS_WRITE_SESSION,
        expires_in: datetime.timedelta = DEFAULT_SESSION_TIMEOUT,
    ) -> CommitID:
        """Checkout a ref (branch, tag, or commit ID) and initialize a new session.

        Args:
            ref: Commit, branch, or tag name

        Returns:
            commit: #CommitID
        """

        return self._synchronize(self._arepo.checkout, ref, session_token=session_token, for_writing=for_writing, expires_in=expires_in)

    def commit(self, message: str, auto_ff: bool = True, checkout_for_writing: bool = DEFAULT_IS_WRITE_SESSION) -> str:
        """Commit this session's changes and start a new session.

        Args:
            message: Commit message
            auto_ff: Whether to automatically fast-forward the repo and retry if the commit fails

        Returns:
            new_commit: ID of new commit
        """

        return self._synchronize(self._arepo.commit, message, auto_ff=auto_ff, checkout_for_writing=checkout_for_writing)

    def fast_forward(self):
        """Fast-forward the session.
        Attempts to update the session base commit to the latest branch tip.
        Will fail if the same paths have been modified in the current session and on the branch.
        """

        return self._synchronize(self._arepo.fast_forward)

    def new_branch(self, branch: str) -> None:
        """Create a new branch based on the current session reference

        Args:
            branch_name: New branch name
        """

        return self._synchronize(self._arepo.new_branch, branch)

    def create_session(
        self,
        ref: str | CommitID = "main",
        for_writing: bool = DEFAULT_IS_WRITE_SESSION,
        expires_in: datetime.timedelta = DEFAULT_SESSION_TIMEOUT,
        message: str | None = None,
    ) -> LocalSession:
        return self._synchronize(self._arepo.create_session, ref=ref, for_writing=for_writing, expires_in=expires_in, message=message)

    def join_session(self, session_id: SessionID) -> LocalSession:
        return self._synchronize(self._arepo.join_session, session_id)

    # TODO: figure out some clever metaclass way of wrapping all of these methods
    # For now it's faster to just plug and chug
    def _set_doc(self, path: Path, *, content: dict) -> None:
        return self._synchronize(self._arepo._set_doc, path, content=content)

    def _set_docs(self, items: Mapping[str, dict]) -> None:
        return self._synchronize(self._arepo._set_docs, items)

    def _get_doc(self, path: Path) -> dict:
        return self._synchronize(self._arepo._get_doc, path)

    def _doc_exists(self, path: Path) -> bool:
        return self._synchronize(self._arepo._doc_exists, path)

    def _get_docs(self, paths: Sequence[str]) -> Mapping[str, dict]:
        return self._synchronize(self._arepo._get_docs, paths)

    def _del_doc(self, path: Path) -> None:
        return self._synchronize(self._arepo._del_doc, path)

    def _del_docs(self, paths: Sequence[str]) -> None:
        return self._synchronize(self._arepo._del_docs, paths)

    def _set_chunk(self, path: Path, *, data: bytes) -> None:
        return self._synchronize(self._arepo._set_chunk, path, data=data)

    def _set_chunks(self, items: Mapping[str, bytes]) -> None:
        return self._synchronize(self._arepo._set_chunks, items)

    def _get_chunk(self, path: Path) -> bytes:
        return self._synchronize(self._arepo._get_chunk, path)

    def _chunk_exists(self, path: Path) -> bool:
        return self._synchronize(self._arepo._chunk_exists, path)

    def _get_chunks(self, paths: Sequence[str]) -> Mapping[str, bytes]:
        return self._synchronize(self._arepo._get_chunks, paths)

    def _del_chunk(self, path: Path) -> None:
        return self._synchronize(self._arepo._del_chunk, path)

    def _del_chunks(self, paths: Sequence[str]) -> None:
        return self._synchronize(self._arepo._del_chunks, paths)

    def _get_chunk_ref(self, path: Path) -> ReferenceData:
        return self._synchronize(self._arepo._get_chunk_ref, path)

    def _set_chunk_ref(self, path: Path, *, reference_data: ReferenceData) -> None:
        return self._synchronize(self._arepo._set_chunk_ref, path, reference_data=reference_data)

    def _set_chunk_refs(self, items: Mapping[Path, ReferenceData]) -> None:
        return self._synchronize(self._arepo._set_chunk_refs, items)

    def _rename(self, src_path: Path, dst_path: Path) -> None:
        return self._synchronize(self._arepo._rename, src_path, dst_path)

    @property
    def store(self) -> ArraylakeStore:
        """Access a Zarr-compatible #ArraylakeStore store object for this repo.

        Example:

        ```python
        repo = Repo("my_org/my_repo")
        group = zarr.open_group(store=repo.store)
        ```
        """
        return ArraylakeStore(self)

    @property
    def root_group(self) -> zarr.Group:
        """Open the Zarr root group of this repo.

        Example:

        ```python
        repo = Repo("my_org/my_repo")
        group = repo.root_group
        group.tree()  # visualize group hierarchy
        ```
        """
        # 1 __contains__ and 1 __getitem__ hit on root_group
        with self._prefetch(["meta/root.group.json"]):
            grp = zarr.open_group(store=self.store, zarr_version=3)
        return grp

    def status(self, limit: int = 1000):
        """Returns the #SessionStatus for the current session.

        Args:
           limit (int): [Optional] The number of modified paths to return. Defaults to 1000, passing 0
           is equivalent to setting no limit."""
        return self._synchronize(self._arepo.status, limit=limit)

    @property
    def commit_log(self):
        return self._synchronize(self._arepo.commit_log)

    def add_virtual_grib(self, grib_uri: str, path: Path) -> None:
        """Add a virtual GRIB2 dataset to the repo.

        Args:
            path: The path within the repo where the virtual dataset should be created.
            grib_uri: The path to the GRIB2 file. Only `s3://` URIs are supported at the moment.
        """
        self._synchronize(self._arepo.add_virtual_grib, grib_uri, path)

    def add_virtual_hdf(self, hdf_uri: str, path: Path) -> None:
        """Add a virtual HDF5 dataset to the arraylake.

        Args:
            hdf_uri: The path to the HDF5 file. Only `s3://` URIs are supported at the moment.
            path: The path with the repo where the virtual HDF5 dataset should be created.
        """
        warnings.warn("Use add_virtual_netcdf instead", FutureWarning)
        self._synchronize(self._arepo.add_virtual_netcdf, hdf_uri, path)

    def add_virtual_netcdf(self, netcdf_uri: str, path: Path, **kwargs) -> None:
        """Add a virtual Netcdf dataset to the repo.

        Args:
            netcdf_uri: The path to the netCDF file. Only `s3://` URIs are supported at the moment.
              Both netCDF4 and netCDF3 files are supported.
            path: The path within the repo where the virtual dataset should be created.
            kwargs: Additional arguments to pass to the kerchunk
              [file format backend](https://fsspec.github.io/kerchunk/reference.html#file-format-backends).
              Do not pass `storage_options` or `inline_threshold`.
        """
        self._synchronize(self._arepo.add_virtual_netcdf, netcdf_uri, path, **kwargs)

    def add_virtual_zarr(self, zarr_uri: str, path: Path) -> None:
        """Add a virtual Zarr dataset to the repo.

        Args:
            zarr_uri: The path to the Zarr store. Only Zarr V2 stores and `s3://` URIs are supported at the moment.
            path: The path within the repo where the virtual dataset should be created.
        """
        self._synchronize(self._arepo.add_virtual_zarr, zarr_uri, path)

    def add_virtual_tiff(self, tiff_uri: str, path: Path, name: str, **kwargs) -> None:
        """Add a virtual TIFF dataset to the repo.
        Args:
            tiff_uri: The path to the TIFF file. Only `s3://` URIs are supported at the moment.
            path: The path within the repo where the virtual dataset should be created.
            name: TIFF files contain bare arrays and no name. You must provide one.
            kwargs: Additional arguments to pass to the kerchunk
                [file format backend](https://fsspec.github.io/kerchunk/reference.html#file-format-backends).
                Do not pass `storage_options` or `inline_threshold`.
        """
        self._synchronize(self._arepo.add_virtual_tiff, tiff_uri, path, name, **kwargs)

    def tree(self, prefix: str = "", *, depth: int = 10, filter: str | None = None) -> Tree:
        """Display this repo's hierarchy as a Rich Tree

        Args:
            prefix: Path prefix
            depth: Maximum depth to descend into the hierarchy
            filter: JMESPath query to subset the tree
        """
        return self._synchronize(self._arepo._tree, prefix=prefix, depth=depth, filter=filter)

    @contextmanager
    def _prefetch(self, paths):
        try:
            self._synchronize(self._arepo._prefetch_docs, paths=paths)
            self._synchronize(self._arepo._prefetch_coordinate_chunk_refs)
            yield
        finally:
            self._arepo._prefetched_docs.clear()
            self._arepo._prefetched_chunk_refs.clear()

    def to_xarray(self, group=None, **kwargs) -> xr.Dataset:
        """Open and decode an Xarray dataset from the Zarr-compatible ArraylakeStore.

        :::note
        There is no need to specify the `zarr_version` or `engine` keyword arguments.
        They are both set by default in this method.
        :::

        Args:
            group: path to the Zarr Group to load the `xarray.Dataset` from
            **kwargs: additional keyword arguments passed to `xarray.open_dataset`

        Returns:
            Dataset: xarray.Dataset
        """

        import xarray

        # check keyword arguments
        if "zarr_version" in kwargs:
            raise ValueError("Setting `zarr_version` is not allowed here. Arraylake only supports `zarr_version=3`")
        if "engine" in kwargs:
            raise ValueError("Setting `engine` is not allowed here. Arraylake only supports `engine='zarr'`")

        logger.debug("pre-fetching for group", group=group)
        prefix = f"{META_ROOT[:-1]}/{group}" if group else META_ROOT[:-1]
        paths, _ = self.store.list_dir(prefix + "/")
        paths += [f"{prefix}.group.json"]
        kwargs.setdefault("consolidated", False)
        with self._prefetch(paths):
            ds = xarray.open_dataset(
                filename_or_obj=self.store,
                group=group,
                engine="zarr",
                zarr_version=3,
                **kwargs,
            )

        return ds

    def filter_metadata(self, filter: str) -> list[str]:
        """Filter repo metadata attributes using a JMSE search string.

        Args:
            filter: JMESPath query to subset the tree

        Returns:
            A list of document paths

        The full JMES spec including examples and an interactive console is available [here](https://jmespath.org/specification.html).

        Some specific examples of queries:

            ```
            "flags[0].spec[0] == 'a'"
            "flags[0].spec[0:2] == ['a', 'b']"
            'flags[0].spec[2] == band'
            "contains(keys(@), 'flags') && contains(keys(@), 'band') && flags[0].spec[2] == band"
            "someNaN == 'NaN'"
            'number >= `3` && number <= `15`'
            '"eo:val" == `12`'
            '"created:at:time" <= `2022-05-01`'
            '(!flags == `5` || flags == `10`) && foo == `10`'
            ```

            And some specific nuances to be aware of:

            1. NaNs are strings, assert for them as follows:

                    "someKey == 'NaN'"

                The following will not match NaN values:

                    "someNaN == NaN"
                    "someNaN == `NaN`"

            2. Comparison of two missing keys is truthy:

                The following will return true if both don't exist on the doc, as null == null

                    'foo == bar'

                Here's a safer way to perform this query:

                    'contains(keys(@), "foo") && contains(keys(@), "bar") && foo == bar'

            3. Keys with special characters should be double quoted

                    '"eo:val" == `12`'

                The following will fail

                    'eo:val == `12`'
        """
        return self._synchronize(self._arepo.filter_metadata, filter)


class ArraylakeStore(StoreV3):  # type: ignore  # no typying info for StoreV3
    """ArrayLake's Zarr Store interface

    This is an implementation of a [Zarr V3 Store](https://zarr-specs.readthedocs.io/en/latest/core/v3.0.html#id14).

    :::note
    This class is not intended to be constructed directly by users. Instead, use the `store` property on the `Repo` class.
    :::

    """

    def __init__(self, repo: Repo):
        self._repo = repo

    def list_prefix(self, prefix: str) -> list[str]:
        """List a prefix in the store

        Args:
            prefix : the path to list

        Returns:
            A list of document paths
        """
        return self._repo._wrap_async_iter(self._repo._arepo._list_prefix, prefix)

    def listdir(self, prefix: str) -> list[str]:
        """List a directory in the store

        Args:
            prefix: the path to list

        Returns:
            A list of document paths
        """
        return self._repo._wrap_async_iter(self._repo._arepo._list_dir, prefix)

    def getsize(self, prefix: str) -> int:
        data_prefix = DATA_ROOT + prefix
        return self._repo._synchronize(self._repo._arepo._getsize, data_prefix)

    def rmdir(self, dir: str) -> None:
        dir = normalize_storage_path(dir)
        meta_dir = (META_ROOT + dir).rstrip("")
        self._repo._synchronize(self._repo._arepo._del_prefix, meta_dir)
        data_dir = (DATA_ROOT + dir).rstrip("")
        self._repo._synchronize(self._repo._arepo._del_prefix, data_dir)

    def __getitem__(self, key) -> bytes:
        """Get a value

        Args:
            key: the path to get

        Returns:
            bytes (metadata or chunk)
        """
        if key == "zarr.json":
            return ENTRY_POINT_METADATA
        logger.debug("__getitem__", path=key, repo=self._repo.repo_name)
        self._validate_key(key)
        if is_chunk_key(key):
            return self._repo._get_chunk(key)
        elif is_meta_key(key):
            doc = self._repo._get_doc(key)
            return json.dumps(doc).encode()
        else:  # pragma: no cover
            # don't expect to ever reach this
            raise KeyError(f"unexpected key: {key}")

    def getitems(self, keys, *, contexts=None, on_error="omit") -> Mapping[str, bytes]:
        """Get multiple items

        Args:
            keys: list of paths to get

        Returns:
            Mapping where keys are paths and values are bytes (metadata or chunks)
        """
        logger.debug("getitems called with ", num_keys=len(keys), repo=self._repo.repo_name)

        if on_error != "omit":  # pragma: no cover
            raise ValueError("Only support on_error='omit' for now")
        for key in keys:
            self._validate_key(key)
        meta_keys, chunk_keys = _sort_keys(keys)
        # TODO: can we have all of the needed queries in flight at the same time?
        # This two-step process is potentially inefficient
        chunk_docs = self._repo._get_chunks(chunk_keys) if chunk_keys else {}
        if "zarr.json" in meta_keys:
            meta_docs = {"zarr.json": ENTRY_POINT_METADATA}
            meta_keys.remove("zarr.json")
        else:
            meta_docs = {}
        if meta_keys:
            meta_docs.update({key: json.dumps(doc).encode() for key, doc in self._repo._get_docs(meta_keys).items()})

        # TODO: use this much better syntax once we drop Python 3.9
        # return meta_docs | chunk_docs
        return {**meta_docs, **chunk_docs}

    def __setitem__(self, key, value: bytes) -> None:
        """Set a value

        Args:
            key: the path to set

        Returns:
            bytes (metadata or chunk)
        """

        self._validate_key(key)
        if is_chunk_key(key):
            return self._repo._set_chunk(key, data=value)
        elif is_meta_key(key):
            if key == "zarr.json":
                raise KeyError("Cannot set zarr.json")
            doc = json.loads(value)
            return self._repo._set_doc(key, content=doc)
        else:
            raise KeyError(f"unexpected key: {key}")

    def setitems(self, items: Mapping[str, bytes]) -> None:
        """Set multiple items

        Args:
            keys : list of paths

        Returns:
            Mapping where keys are paths and values are bytes (metadata or chunks)
        """

        for key in items:
            self._validate_key(key)
        meta_keys, chunk_keys = _sort_keys(list(items))
        meta_docs = {key: json.loads(items[key]) for key in meta_keys}
        chunk_docs = {key: items[key] for key in chunk_keys}
        # It is important that we set the metadata docs before the chunk docs so that the /data node will be set first
        if meta_docs:
            self._repo._set_docs(meta_docs)
        if chunk_docs:
            self._repo._set_chunks(chunk_docs)

    def __delitem__(self, key):
        """Delete a key.

        Args:
            key: path to delete
        """
        self._validate_key(key)
        if is_chunk_key(key):
            return self._repo._del_chunk(key)
        elif is_meta_key(key):
            return self._repo._del_doc(key)
        else:  # pragma: no cover
            raise KeyError(f"unexpected key: {key}")

    def delitems(self, keys) -> None:
        """Delete multiple keys

        Args:
            keys: list of paths to delete
        """

        for key in keys:
            self._validate_key(key)
        meta_keys, chunk_keys = _sort_keys(keys)
        # TODO: can we have all of the needed queries in flight at the same time?
        # This two-step process is potentially inefficient
        if chunk_keys:
            self._repo._del_chunks(chunk_keys)
        if meta_keys:
            self._repo._del_docs(meta_keys)

    def __contains__(self, key: str) -> bool:
        """check if key exists in store.

        Args:
            key: path to check
        """
        # fast path for a query that Zarr does over and over again
        if key == "zarr.json":
            return True
        logger.debug("__contains__", path=key, repo=self._repo.repo_name)
        try:
            self._validate_key(key)
        except ValueError:
            return False
        if is_chunk_key(key):
            return self._repo._chunk_exists(key)
        elif is_meta_key(key):
            return self._repo._doc_exists(key)
        else:  # pragma: no cover
            # this should never actually happen because a valid key will always resolve
            # to either a meta key or a chunk key
            return False

    def keys(self) -> list[str]:
        """Return a list of this store's keys"""

        return self.list_prefix("")

    def __iter__(self):
        """Iterate over this store's keys"""

        yield from self.keys()

    def erase_prefix(self, prefix):
        """Erase all keys with the given prefix."""
        self._repo._synchronize(self._repo._arepo._del_prefix, prefix)

    def __len__(self) -> int:
        """number of keys in this store"""
        # TODO: this is a very inefficient way to do this
        # we should consider more efficient implementations
        return len(self.keys())

    def rename(self, src_path: Path, dst_path: Path) -> None:
        self._repo._rename(src_path, dst_path)

    def __getattribute__(self, name):
        """Influence upstream Zarr by failing a hasattr check for `get_partial_values`.

        Doing so forces it to use a preferable code path for retrieving data (getitems). See:
        https://github.com/zarr-developers/zarr-python/blob/a81db0782535ba04c32c277102a6457d118a73e8/zarr/core.py#L2162-L2171
        """
        if name == "get_partial_values":
            raise AttributeError
        return super().__getattribute__(name)


@dataclass
class SessionStatus:
    """Holds the status of a session."""

    repo_name: str
    """Name of the repo"""
    session: LocalSession
    """#LocalSession object."""
    modified_paths: list[tuple[Path, bool]]
    """List of modified paths and whether they were deleted."""

    def rich_output(self, console=None):
        from rich.console import Console
        from rich.panel import Panel

        if console is None:
            console = Console()

        console.print(f":ice: Using repo [bold]{self.repo_name}[/bold]")
        console.print(f":pager: Session [bold]{self.session.id}[/bold] started at {self.session.start_time}")
        if self.session.branch:
            console.print(f":herb: On branch [bold]{self.session.branch}[/bold]")
        else:
            console.print(":shrug: Not on a branch")

        changes = []
        for path, deleted in self.modified_paths:
            if deleted:
                changes.append(f":cross_mark: [red]{path}[/red]")
            else:
                changes.append(f":pencil: [green]{path}[/green]")

        if changes:
            console.print(Panel("\n".join(changes), title="paths modified in session", title_align="left", expand=False, padding=(1, 2)))
        else:
            console.print("No changes in current session.")

    def _repr_html_(self):
        html = "<p>\n"
        html += f"🧊 Using repo <b>{escape(self.repo_name)}</b><br />\n"
        html += f"📟 Session <b>{escape(self.session.id)}</b> started at <i>{escape(self.session.start_time.isoformat())}</i><br />\n"
        if self.session.branch:
            html += f"🌿 On branch <b>{escape(self.session.branch)}</b><br />\n"
        else:
            html += "🤷 Not on a branch<br />\n"
        html += "</p>\n"

        changes = []
        for path, deleted in self.modified_paths:
            if deleted:
                changes.append(f"""  <li style="color: red; list-style: none;">❌ {escape(path)}</li>\n""")
            else:
                changes.append(f"""  <li style="color: green; list-style: none;">📝 {escape(path)}</li>\n""")

        if changes:
            html += """<div style="border: 1px dashed gray; border-radius: 5px; padding: 1em;">\n"""
            html += """ <h3>paths modified in session</h3>\n <ul>\n"""
            html += "".join(changes)
            html += """ </ul>\n</div>"""
        else:
            html += "<p>No changes in current session</p>\n"
        return html
