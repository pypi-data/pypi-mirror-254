import asyncio
import socket
import weakref
from collections.abc import Mapping
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal, Optional

import aiobotocore.client
import aiobotocore.session
import aiohttp
import botocore
import urllib3
from aiobotocore.config import AioConfig
from botocore import UNSIGNED

from arraylake.api_utils import retry_on_exception
from arraylake.asyn import close_async_context, get_loop, sync
from arraylake.chunkstore.abc import ObjectStore
from arraylake.log_util import get_logger

if TYPE_CHECKING:
    from types_aiobotocore_s3 import S3Client


logger = get_logger(__name__)


# This is copied from fsspec
# https://github.com/fsspec/s3fs/blob/34a32198188164fd48d4d1abcb267f033d1d1ce1/s3fs/core.py#L63
S3_RETRYABLE_ERRORS = (
    socket.timeout,
    botocore.exceptions.HTTPClientError,
    urllib3.exceptions.IncompleteRead,
    botocore.parsers.ResponseParserError,
    aiohttp.ClientPayloadError,
)


# Below we set up a global cache for aiobotocore clients
# There should be one per each event loop and set of configuration parameters
# dicts aren't hashable, so we sort the keywords into key / value pairs
@dataclass(eq=True, frozen=True)
class ClientKey:
    loop: asyncio.AbstractEventLoop
    client_kwargs: tuple[tuple[str, str], ...]


# tried making these weakref.WeakValueDictionary(), but they were getting garbage collected too early
# TODO: investigate whether use of weakref would be more efficient here
# As is, the clients are cleaned up at the end of the python interpreter session.
_GLOBAL_CLIENTS: dict[ClientKey, "S3Client"] = {}

# this is a cache to use hold asyncio tasks so they are not garbage collected before finishing
background_tasks: set[asyncio.Task] = set()


async def get_client(loop: asyncio.AbstractEventLoop, **client_kws) -> "S3Client":
    """
    Attempt to get an aws client for a specific event loop and set of parameters.
    If the client already exists, the global cache will be used.
    If not, a new client will be created.
    """

    key = ClientKey(loop, tuple(sorted(client_kws.items())))
    logger.debug("%d s3 clients present in cache.", len(_GLOBAL_CLIENTS))
    if key not in _GLOBAL_CLIENTS:
        logger.debug("Creating new s3 client %s. Loop id %s.", key, id(loop))
        anon = client_kws.pop("anon", False)
        if anon:
            client_kws["config"] = AioConfig(signature_version=UNSIGNED)
        client_creator: "S3Client" = aiobotocore.session.get_session().create_client("s3", **client_kws)
        new_client = await client_creator.__aenter__()
        weakref.finalize(new_client, close_client, key)
        _GLOBAL_CLIENTS[key] = new_client
    else:
        logger.debug("Client %s already present. Loop id %s.", key, id(loop))
    return _GLOBAL_CLIENTS[key]


def close_client(key: ClientKey) -> None:
    """
    This is a finalizer function that is called when a global client is
    garbage collected. It cleanly closes the client for the specified key.

    If the event loop associated with this client is already closed, we can't
    call __aexit__. So we attempt to directly close the TCP Socket associated
    with the aiohttp session.

    If the event loop associated with this client is determined to be the
    dedicated io loop, we call `sync` to on __aexit__.

    If the event loop associated with this client is determined to be the currently
    running event loop, we schedule the __aexit__ coroutine for execution.

    If the event loop doesn't match any of these scenarios, we have no way to call
    the closer function and issue a RuntimeWarning

    Note: logging in this function runs the risk of conflicting with pytest#5502. For
    this reason, we have removed debug log statements.
    """
    client = _GLOBAL_CLIENTS.pop(key)

    client_loop = key.loop  # the loop this client was created from

    if not hasattr(client, "_endpoint"):
        return  # this makes mypy happy

    # this is the underlying thing we have to close
    aio_http_session = client._endpoint.http_session._session
    # sanity checks
    # assert aio_http_session._loop is client_loop
    # assert aio_http_session._connector._loop is client_loop

    if aio_http_session.closed:
        return

    sync_loop = get_loop()  # the loop associated with the synchronizer thread

    try:
        running_loop = asyncio.get_running_loop()
    except RuntimeError:
        running_loop = None

    if client_loop.is_closed():
        # we can never talk to this client again because its loop is closed;
        # just close the sockets directly
        aio_http_session._connector._close()
        assert aio_http_session.closed
    else:
        # client loop is still open -- how can we talk to it?
        if client_loop is sync_loop:
            sync(close_async_context, client, "calling from sync", timeout=1)
        elif client_loop is running_loop:
            coro = close_async_context(client, f"closing from loop {id(client_loop)}")
            if client_loop.is_running():
                task = client_loop.create_task(coro)
                # try to prevent this task from being garbage collected before it finishes
                background_tasks.add(task)
            else:
                client_loop.run_until_complete(coro)


class S3ObjectStore(ObjectStore):
    _OPEN: bool
    _session_client: Optional["S3Client"]
    _bucket_name: str
    client_kws: Mapping[str, str]

    def __init__(self, bucket_name, client_kws):
        self._bucket_name = bucket_name.strip("/")
        self.client_kws = client_kws
        self._set_props()

    @property
    def bucket_name(self) -> str:
        return self._bucket_name

    def _set_props(self):
        self._session_client = None

    def __getstate__(self):
        return self._bucket_name, self.client_kws

    def __setstate__(self, state):
        self._bucket_name, self.client_kws = state
        self._set_props()

    async def _open(self):
        if self._session_client is not None:
            return
        loop = asyncio.get_running_loop()
        self._session_client = await get_client(loop, **self.client_kws)

    def make_uri(self, key: str) -> str:
        return f"s3://{self.bucket_name}/{key}"

    @property
    def status(self) -> Literal["OPEN", "CLOSED"]:
        return "OPEN" if self._session_client is not None else "CLOSED"

    async def ping(self):
        """Check if the chunk store bucket exists."""
        await self._open()
        # Mypy cannot tell that self._session_cleint is not None (set it self._open())
        # Note: this can likely be removed once we drop support for Python 3.8
        if self._session_client is None:
            raise ValueError("session client not set")
        # TODO: Should raise an exception if the bucket does not exist
        await self._session_client.head_bucket(Bucket=self.bucket_name)

    @retry_on_exception(S3_RETRYABLE_ERRORS, n=5)
    async def put_data(self, *, data: bytes, key: str) -> None:
        await self._open()
        # Mypy cannot tell that self._session_client is not None (set it self._open())
        # Note: this can likely be removed once we drop support for Python 3.8
        if self._session_client is None:
            raise ValueError("session client not set")
        resp = await self._session_client.put_object(Bucket=self.bucket_name, Key=key, Body=data)
        await logger.adebug("put_data received response: %s", resp)

    @retry_on_exception(S3_RETRYABLE_ERRORS, n=5)
    async def pull_data(self, start_byte: int, length: int, key: str, bucket: str) -> bytes:
        await self._open()
        # Mypy cannot tell that self._session_client is not None (set it self._open())
        # Note: this can likely be removed once we drop support for Python 3.8
        if self._session_client is None:
            raise ValueError("session client not set")
        # stop_byte is inclusive, in contrast to python indexing conventions
        # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Range
        stop_byte = start_byte + length - 1
        byte_range = f"bytes={start_byte}-{stop_byte}"
        response = await self._session_client.get_object(Bucket=bucket, Key=key, Range=byte_range)
        await logger.adebug("pull_data received response: %s", response)
        async with response["Body"] as stream:
            data = await stream.read()
        return data

    @property
    async def is_anonymous_session(self):
        await self._open()
        # Mypy cannot tell that self._session_client is not None (set it self._open())
        # Note: this can likely be removed once we drop support for Python 3.8
        if self._session_client is None:
            raise ValueError("session client not set")
        # TODO: Does _client_config always exist
        return self._session_client._client_config.signature_version == botocore.UNSIGNED  # type: ignore

    def __repr__(self):
        status = self.status
        disp = f"{type(self).__name__}, bucket: {self.bucket_name}, status: {status}"
        if status == "OPEN":
            assert self._session_client is not None
            if hasattr(self._session_client, "_endpoint"):
                disp += f", endpoint: {self._session_client._endpoint.host}"
                # f"auth_method: {self._fs.credentials.method!r}"
            disp += f", client_kws: {self.client_kws}"
        return disp
