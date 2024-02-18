from __future__ import annotations

import os
from collections.abc import AsyncGenerator, Generator, Mapping, Sequence
from dataclasses import dataclass, field
from typing import Any, TypeVar

from pydantic import TypeAdapter

from arraylake.api_utils import (
    ArraylakeHttpClient,
    gather_and_check_for_exceptions,
    handle_response,
)
from arraylake.asyn import gather_with_throttled_concurrency
from arraylake.metastore.abc import Metastore, MetastoreDatabase
from arraylake.types import (
    Branch,
    BranchName,
    BulkCreateDocBody,
    CollectionName,
    Commit,
    CommitID,
    DocResponse,
    DocSessionsResponse,
    NewCommit,
    NewSession,
    Path,
    PathSizeResponse,
    Repo,
    RepoCreateBody,
    SessionExpirationUpdate,
    SessionID,
    SessionInfo,
    SessionPathsResponse,
    Tag,
    Tree,
    UpdateBranchBody,
)

BATCH_SIZE = int(os.environ.get("ARRAYLAKE_BATCH_SIZE", 20))
THROTTLE_CONCURRENCY_SIZE = int(os.environ.get("ARRAYLAKE_THROTTLE_CONCURRENCY_SIZE", 4))

# type adapters
LIST_DATABASES_ADAPTER = TypeAdapter(list[Repo])
GET_COMMITS_ADAPTER = TypeAdapter(list[Commit])
GET_TAGS_ADAPTER = TypeAdapter(list[Tag])
GET_BRANCHES_ADAPTER = TypeAdapter(list[Branch])
GET_ALL_SESSIONS_FOR_PATH_ADAPTER = TypeAdapter(list[DocSessionsResponse])
GET_ALL_PATHS_FOR_SESSION_ADAPTER = TypeAdapter(list[SessionPathsResponse])
GET_DOCS_ADAPTER = TypeAdapter(list[DocResponse])
LIST_OF_PATHS_ADAPTER = TypeAdapter(list[Path])
ADD_DOCS_ADAPTER = TypeAdapter(list[BulkCreateDocBody])

T = TypeVar("T")


def chunks(seq: Sequence[T], size: int) -> Generator[Sequence[T], None, None]:
    return (seq[pos : (pos + size)] for pos in range(0, len(seq), size))  # noqa: E203


@dataclass
class HttpMetastoreConfig:
    """Encapsulates the configuration for the HttpMetastore"""

    api_service_url: str
    org: str
    token: str | None = field(default=None, repr=False)  # machine token. id/access/refresh tokens are managed by CustomOauth
    auth_org: str | None = None
    managed_sessions: bool = False


class HttpMetastore(ArraylakeHttpClient, Metastore):
    """ArrayLake's HTTP Metastore

    This metastore connects to ArrayLake over HTTP

    args:
        config: config for the metastore

    :::note
    Authenticated calls require an Authorization header. Run ``arraylake auth login`` to login before using this metastore.
    :::
    """

    _config: HttpMetastoreConfig

    def __init__(self, config: HttpMetastoreConfig):
        super().__init__(config.api_service_url, token=config.token, hint=config.auth_org, managed_sessions=config.managed_sessions)

        self._config = config
        self.api_url = config.api_service_url

    async def ping(self) -> dict[str, Any]:
        response = await self._request("GET", "user")
        handle_response(response)

        return response.json()

    async def list_databases(self) -> list[Repo]:
        response = await self._request("GET", f"/orgs/{self._config.org}/repos")
        handle_response(response)
        return LIST_DATABASES_ADAPTER.validate_json(response.content)

    async def create_database(self, name: str, bucket_nickname: str | None = None):
        """
        Params:
          - bucket_nickname: optional nickname of a bucket already existing in the org.
            If this argument is passed, all reads and writes to the repository will direct
            chunks to this bucket, without using the local chunkstore configuration.
        """
        body = RepoCreateBody(name=name, bucket_nickname=bucket_nickname)
        response = await self._request("POST", f"/orgs/{self._config.org}/repos", content=body.model_dump_json())
        handle_response(response)
        # TODO: we shouldn't need to make another request to get the repo (in open_database), the response body has everything we need
        # either stop shipping the repo body back in the POST request or bypass the GET request in open_database
        return await self.open_database(name)

    async def open_database(self, name: str) -> HttpMetastoreDatabase:
        # verify repo actually exists
        response = await self._request("GET", f"/repos/{self._config.org}/{name}")
        handle_response(response)  # raise error on 404
        db_config = HttpMetastoreDatabaseConfig(
            http_metastore_config=self._config,
            repo=name,
        )
        return HttpMetastoreDatabase(db_config)

    async def delete_database(self, name: str, *, imsure: bool = False, imreallysure: bool = False) -> None:
        if not (imsure and imreallysure):
            raise ValueError("Don't do this unless you're really sure. Once the database has been deleted, it's gone forever.")

        response = await self._request("DELETE", f"/orgs/{self._config.org}/{name}")
        handle_response(response)


@dataclass
class HttpMetastoreDatabaseConfig:
    """Encapsulates the configuration for an HttpMetastoreDatabase"""

    http_metastore_config: HttpMetastoreConfig
    repo: str


class HttpMetastoreDatabase(ArraylakeHttpClient, MetastoreDatabase):
    _config: HttpMetastoreDatabaseConfig

    def __init__(self, config: HttpMetastoreDatabaseConfig):
        """ArrayLake's HTTP Metastore Database

        This metastore database connects to ArrayLake over HTTP

        args:
            config: config for the metastore database

        :::note
        Authenticated calls require an Authorization header. Run ``arraylake auth login`` to login before using this metastore.
        :::
        """
        super().__init__(
            config.http_metastore_config.api_service_url,
            token=config.http_metastore_config.token,
            hint=config.http_metastore_config.auth_org,
        )

        self._config = config
        self._setup()

    def _setup(self):
        self._repo_path = f"/repos/{self._config.http_metastore_config.org}/{self._config.repo}"

    def __getstate__(self):
        return self._config

    def __setstate__(self, state):
        super().__init__(
            state.http_metastore_config.api_service_url, token=state.http_metastore_config.token, hint=state.http_metastore_config.auth_org
        )
        self._config = state
        self._setup()

    def __repr__(self):
        status = "OPEN" if self._client is not None else "CLOSED"
        full_name = f"{self._config.http_metastore_config.org}/{self._config.repo}"
        return f"<arraylake.http_metastore.HttpMetastoreDatabase repo_name='{full_name}' status={status}>"

    async def get_commits(self) -> tuple[Commit, ...]:
        response = await self._request("GET", f"{self._repo_path}/commits")
        handle_response(response)
        return tuple(GET_COMMITS_ADAPTER.validate_json(response.content))

    async def get_commit_by_id(self, commit_id: CommitID) -> Commit:
        response = await self._request("GET", f"{self._repo_path}/commits/{commit_id}")
        handle_response(response)
        return Commit.model_validate_json(response.content)

    async def get_tags(self) -> tuple[Tag, ...]:
        response = await self._request("GET", f"{self._repo_path}/tags")
        handle_response(response)
        return tuple(GET_TAGS_ADAPTER.validate_json(response.content))

    async def get_branches(self, names: Sequence[BranchName] = []) -> tuple[Branch, ...]:
        params = {"names": names} if names else {}
        response = await self._request("GET", f"{self._repo_path}/branches", params=params)
        handle_response(response)
        return tuple(GET_BRANCHES_ADAPTER.validate_json(response.content))

    async def get_refs(self) -> tuple[tuple[Tag, ...], tuple[Branch, ...]]:
        return await gather_and_check_for_exceptions(self.get_tags(), self.get_branches())

    async def new_commit(self, commit_info: NewCommit) -> CommitID:
        response = await self._request("PUT", f"{self._repo_path}/commits", content=commit_info.model_dump_json())
        handle_response(response)
        return CommitID.fromhex(response.json()["_id"])

    async def old_style_rebase(self, commit_id: CommitID, upstream_branch: BranchName) -> CommitID:
        """Old method, needed for tests and compatibility with clients <= 0.7.6

        Delete this method once arraylake 0.7.6 is no longer supported
        """
        body = {"commit_id": str(commit_id) if commit_id else None, "branch_name": upstream_branch}
        response = await self._request("POST", f"{self._repo_path}/rebase", params=body)
        handle_response(response)
        return CommitID.fromhex(response.json()["commit_id"])

    async def rebase(self, base_commit: CommitID | None, session_id: SessionID, upstream_branch: BranchName) -> CommitID:
        body = {"session_id": str(session_id), "branch_name": upstream_branch}
        # passing base_commit=& as query parameter doesn't work, it gets parsed as an empty DBID
        if base_commit is not None:
            body["base_commit"] = str(base_commit)

        response = await self._request("POST", f"{self._repo_path}/rebase", params=body)
        handle_response(response)
        return CommitID.fromhex(response.json()["commit_id"])

    # TODO: Make session_id mandatory once all clients are using
    # managed_sessions by default.
    async def update_branch(
        self,
        branch: BranchName,
        *,
        session_id: SessionID | None,
        base_commit: CommitID | None,
        new_commit: CommitID,
        new_branch: bool = False,
    ) -> None:
        body = UpdateBranchBody(branch=branch, session_id=session_id, new_commit=new_commit, base_commit=base_commit, new_branch=new_branch)
        response = await self._request("PUT", f"{self._repo_path}/branches", content=body.model_dump_json())
        handle_response(response)

    # FIXME: Do we need to re-home this, since it collides with the /sessions
    # path prefix?
    async def get_all_sessions_for_path(self, path: Path, *, collection: CollectionName) -> AsyncGenerator[DocSessionsResponse, None]:
        # keys are sids, values are deleted or not
        response = await self._request("GET", f"{self._repo_path}/sessions/{collection}/{path}")
        handle_response(response)

        # TODO: stream/paginate here
        docs = GET_ALL_SESSIONS_FOR_PATH_ADAPTER.validate_json(response.content)
        for doc in docs:
            yield doc

    async def get_all_paths_for_session(
        self,
        session_id: SessionID,
        base_commit: CommitID | None,
        *,
        collection: CollectionName,
        limit: int = 0,
    ) -> AsyncGenerator[SessionPathsResponse, None]:
        """Get all paths that have been modified in the current session."""

        # /repos/{org}/{repo}/sessions/{collection}/{session_id}
        params = {"limit": limit, "session_id": session_id, "base_commit": base_commit}
        response = await self._request("GET", f"{self._repo_path}/modified_paths/{collection}", params=params)
        handle_response(response)

        # TODO: stream/paginate here
        docs = GET_ALL_PATHS_FOR_SESSION_ADAPTER.validate_json(response.content)
        for doc in docs:
            yield doc

    async def get_all_paths_for_commit(
        self,
        commit_id: CommitID,
        *,
        collection: CollectionName,
        limit: int = 0,
    ) -> AsyncGenerator[SessionPathsResponse, None]:
        params = {"limit": limit, "commit_id": commit_id}
        response = await self._request("GET", f"{self._repo_path}/modified_paths_commit/{collection}", params=params)
        handle_response(response)

        # TODO: stream/paginate here
        docs = GET_ALL_PATHS_FOR_SESSION_ADAPTER.validate_json(response.content)
        for doc in docs:
            yield doc

    async def create_session(self, session_request: NewSession) -> SessionInfo:
        response = await self._request("POST", f"{self._repo_path}/sessions", content=session_request.model_dump_json())
        handle_response(response)

        return SessionInfo.model_validate_json(response.content)

    async def get_session(self, session_id: SessionID) -> SessionInfo:
        response = await self._request("GET", f"{self._repo_path}/sessions/{session_id}")
        handle_response(response)

        return SessionInfo.model_validate_json(response.content)

    async def update_session_expiration(self, update_request: SessionExpirationUpdate) -> SessionInfo:
        response = await self._request(
            "PUT", f"{self._repo_path}/sessions/{update_request.session_id}", content=update_request.model_dump_json()
        )
        handle_response(response)

        return SessionInfo.model_validate_json(response.content)

    async def expire_session(self, session_id: SessionID) -> SessionInfo:
        response = await self._request("DELETE", f"{self._repo_path}/sessions/{session_id}")
        handle_response(response)

        return SessionInfo.model_validate_json(response.content)

    async def _add_docs(
        self, docs: Sequence[BulkCreateDocBody], collection: CollectionName, session_id: SessionID, base_commit: CommitID | None
    ) -> None:
        """Submits a list of docs to the server to be added in bulk."""
        params = {"session_id": session_id, "base_commit": str(base_commit) if base_commit else None}
        content = ADD_DOCS_ADAPTER.dump_json(list(docs))
        response = await self._request("PUT", f"{self._repo_path}/contents/{collection}/_bulk_set", content=content, params=params)
        handle_response(response)

    async def add_docs(
        self, items: Mapping[Path, Mapping[str, Any]], *, collection: CollectionName, session_id: SessionID, base_commit: CommitID | None
    ) -> None:
        docs = [BulkCreateDocBody(session_id=session_id, content=content, path=path) for path, content in items.items()]
        await gather_and_check_for_exceptions(
            *[
                self._add_docs(docs=batch, collection=collection, session_id=session_id, base_commit=base_commit)
                for batch in chunks(docs, BATCH_SIZE)
            ]
        )

    async def del_docs(
        self, paths: Sequence[Path], *, collection: CollectionName, session_id: SessionID, base_commit: CommitID | None
    ) -> None:
        params = {"session_id": session_id, "base_commit": base_commit}
        content = LIST_OF_PATHS_ADAPTER.dump_json(list(paths))
        response = await self._request("PUT", f"{self._repo_path}/contents/{collection}/_bulk_delete", content=content, params=params)
        handle_response(response)

    async def _get_docs(
        self, paths: Sequence[Path], collection: CollectionName, session_id: SessionID, base_commit: CommitID | None
    ) -> list[DocResponse]:
        """Submits a list of paths to the server to be retrieved in bulk."""
        params = {"session_id": session_id, "base_commit": str(base_commit) if base_commit else None}
        content = LIST_OF_PATHS_ADAPTER.dump_json(list(paths))
        response = await self._request("POST", f"{self._repo_path}/contents/{collection}/_bulk_get", content=content, params=params)
        handle_response(response)
        return GET_DOCS_ADAPTER.validate_json(response.content)

    async def get_docs(
        self, paths: Sequence[Path], *, collection: CollectionName, session_id: SessionID, base_commit: CommitID | None
    ) -> AsyncGenerator[DocResponse, None]:
        # remove dupes from request; is there a cheaper way of doing this? seems like a lot of overhead for every call
        paths = list(set(paths))

        results = await gather_with_throttled_concurrency(
            THROTTLE_CONCURRENCY_SIZE,
            *(
                self._get_docs(paths_batch, collection, session_id=session_id, base_commit=base_commit)
                for paths_batch in chunks(paths, BATCH_SIZE)
            ),
        )

        for result in results:
            for doc in result:
                yield doc

    # TODO: could make list cacheable if we can bound it on a specific commit
    async def list(
        self,
        prefix: str,
        *,
        collection: CollectionName,
        session_id: SessionID,
        base_commit: CommitID | None,
        all_subdirs: bool = False,
        filter: str | None = None,
    ) -> AsyncGenerator[Path, None]:
        # TODO: implement pagination for this API call
        response = await self._request(
            "GET",
            f"{self._repo_path}/contents/{collection}/",
            params={
                "prefix": prefix,
                "session_id": session_id,
                "base_commit": str(base_commit) if base_commit else None,
                "all_subdirs": all_subdirs,
                "filter": filter,
            },
        )
        handle_response(response)

        # TODO: stream or paginate this
        paths = LIST_OF_PATHS_ADAPTER.validate_json(response.content)
        for path in paths:
            yield path

    async def getsize(
        self,
        prefix: str,
        *,
        session_id: SessionID,
        base_commit: CommitID | None,
    ) -> PathSizeResponse:
        response = await self._request(
            "GET",
            f"{self._repo_path}/size/",
            params={"prefix": prefix, "session_id": session_id, "base_commit": str(base_commit) if base_commit else None},
        )
        handle_response(response)
        return PathSizeResponse.model_validate_json(response.content)

    async def del_prefix(self, prefix: str, *, collection: CollectionName, session_id: SessionID, base_commit: CommitID | None) -> None:
        response = await self._request(
            "DELETE",
            f"{self._repo_path}/contents/{collection}/{prefix}",
            params={"session_id": session_id, "base_commit": str(base_commit) if base_commit else None},
        )
        handle_response(response)

    async def tree(
        self,
        prefix: str,
        *,
        session_id: SessionID,
        base_commit: CommitID | None,
        depth: int = 10,
        filter: str | None = None,
    ) -> Tree:
        response = await self._request(
            "GET",
            f"{self._repo_path}/tree",
            params={
                "prefix": prefix,
                "session_id": session_id,
                "base_commit": str(base_commit) if base_commit else None,
                "depth": depth,
                "filter": filter,
            },
        )
        handle_response(response)
        return Tree.model_validate_json(response.content)

    async def rename(
        self,
        src_path: Path,
        dst_path: Path,
        *,
        session_id: SessionID,
        base_commit: CommitID | None,
    ) -> None:
        params = {
            "src_path": src_path,
            "dst_path": dst_path,
            "session_id": session_id,
            "base_commit": str(base_commit) if base_commit else None,
        }
        response = await self._request(
            "PUT",
            f"{self._repo_path}/contents/nodes/rename",
            params=params,
        )
        handle_response(response)

    async def delete_branch(self, branch_name: BranchName) -> bool:
        raise NotImplementedError("Branch delete not supported")
