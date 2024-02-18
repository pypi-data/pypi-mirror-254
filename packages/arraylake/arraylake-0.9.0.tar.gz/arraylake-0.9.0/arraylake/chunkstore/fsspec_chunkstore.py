import asyncio
from collections.abc import Mapping
from enum import Enum
from typing import Literal, Optional

import fsspec
from fsspec import AbstractFileSystem

from arraylake.chunkstore.abc import ObjectStore
from arraylake.log_util import get_logger


class Platform(Enum):
    S3 = 1
    GS = 2


logger = get_logger(__name__)


class FSSpecObjectStore(ObjectStore):
    _OPEN: bool
    _fs: Optional[AbstractFileSystem]
    _bucket_name: str
    protocol: Literal["gs", "s3"]
    client_kws: Mapping[str, str]

    def __init__(self, bucket_name: str, client_kws: Mapping[str, str], platform: Platform):
        self._bucket_name = bucket_name
        self.client_kws = client_kws
        if platform == Platform.S3:
            self.protocol = "s3"
        elif platform == Platform.GS:
            self.protocol = "gs"
        self._fs = None

    @property
    def bucket_name(self) -> str:
        return self._bucket_name

    async def _open(self):
        """
        We need to do something to actually open a session.
        This is important. We need to create the connection in the current loop.
        Otherwise all hell breaks loose. This also means we need to call ._open() on
        every op.
        """
        loop = asyncio.get_running_loop()
        if self._fs is None:
            self._fs = fsspec.get_filesystem_class(self.protocol)(loop=loop, **self.client_kws)
        assert self._fs.loop is loop

    def __getstate__(self):
        return self._bucket_name, self.protocol, self.client_kws

    def __setstate__(self, state):
        self._bucket_name, self.protocol, self.client_kws = state
        # TODO: figure out how to pickle *async* fsspec filesystem objects
        # TypeError: no default __reduce__ due to non-trivial __cinit__
        self._fs = None

    def make_uri(self, key: str):
        return f"{self.protocol}://{self.bucket_name}/{key}"

    @property
    def status(self) -> Literal["OPEN", "CLOSED"]:
        raise NotImplementedError

    async def ping(self):
        raise NotImplementedError

    async def pull_data(self, start_byte: int, length: int, key: str, bucket: str) -> bytes:
        await self._open()
        assert self._fs is not None  # for mypy
        # stop_byte is inclusive, in contrast to python indexing conventions
        # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Range
        stop_byte = start_byte + length  # - 1
        data = await self._fs._cat_file(f"{bucket}/{key}", start=start_byte, end=stop_byte)
        return data

    async def put_data(self, *, data: bytes, key: str) -> None:
        await self._open()
        assert self._fs is not None  # for mypy
        resp = await self._fs._pipe_file(path=f"{self.bucket_name}/{key}", data=data)
        await logger.adebug("put_data received response: %s", resp)

    @property
    async def is_anonymous_session(self):
        raise NotImplementedError


class S3FSObjectStore(FSSpecObjectStore):
    """This is a reference implementation."""

    def __init__(self, bucket_name: str, client_kws: Mapping[str, str]):
        super().__init__(bucket_name=bucket_name, client_kws=client_kws, platform=Platform.S3)

    async def _open(self):
        await super()._open()
        assert self._fs is not None
        # s3fs interface is not consistent with gcsfs (╯°益°)╯彡┻━┻
        await self._fs.set_session()
        assert self._fs._s3 is not None

    async def ping(self):
        """Check if the chunk store bucket exists."""
        await self._open()
        assert self._fs is not None
        # TODO: Should raise an exception if the bucket does not exist
        await self._fs._s3.head_bucket(Bucket=self.bucket_name)

    @property
    async def is_anonymous_session(self) -> bool:
        self._open()
        assert self._fs is not None
        return self._fs._s3.anon is True

    @property
    def status(self) -> Literal["OPEN", "CLOSED"]:
        return "OPEN" if self._fs is not None and self._fs._s3 is not None else "CLOSED"

    def __repr__(self):
        status = self.status
        disp = f"{type(self).__name__}, bucket: {self.bucket_name}, status: {status}"
        if status == "OPEN":
            assert self._fs is not None
            disp += f", endpoint: {self._fs._s3._endpoint}, anonymous?: {self._fs.anon}"
        return disp


class GCSFSObjectStore(FSSpecObjectStore):
    def __init__(self, bucket_name: str, client_kws: Mapping[str, str]):
        super().__init__(bucket_name=bucket_name, client_kws=client_kws, platform=Platform.GS)

    @property
    def status(self) -> Literal["OPEN", "CLOSED"]:
        return "OPEN" if self._fs is not None and self._fs._session is not None else "CLOSED"

    async def _open(self):
        await super()._open()
        assert self._fs is not None
        # s3fs interface is not consistent with gcsfs (╯°益°)╯彡┻━┻
        await self._fs._set_session()
        assert self._fs._session is not None

    async def ping(self):
        """Check if the chunk store bucket exists."""
        await self._open()
        assert self._fs is not None
        assert await self._fs._exists(self.bucket_name)

    def __repr__(self):
        status = self.status
        disp = f"{type(self).__name__}, bucket: {self.bucket_name}, status: {status}"
        if status == "OPEN":
            assert self._fs is not None
            disp += f", endpoint: {self._fs._endpoint}, auth_method: {self._fs.credentials.method!r}"
        return disp

    @property
    async def is_anonymous_session(self) -> bool:
        await self._open()
        assert self._fs is not None
        credentials = self._fs.credentials
        return credentials.method is None and credentials.token == "anonymous"
