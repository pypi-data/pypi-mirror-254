import base64
import importlib
from functools import lru_cache
from typing import Callable, Optional
from urllib.parse import urlparse

import cachetools
import numpy as np

from arraylake.chunkstore.abc import Chunkstore, ObjectStore
from arraylake.config import config
from arraylake.log_util import get_logger
from arraylake.types import ChunkHash, ChunkstoreSchemaVersion, ReferenceData, SessionID

logger = get_logger(__name__)

MAX_INLINE_THRESHOLD_BYTES = 512
KEY_CACHE_SIZE = 5000


class InlineTooLongError(ValueError):
    pass


def decode_inline_data(data: bytes) -> str:
    """called before writing inline data to json"""
    # matches kerchunk inline output
    try:
        dec = data.decode()
    except UnicodeDecodeError:
        dec = "base64:" + base64.b64encode(data).decode()

    if len(dec) > MAX_INLINE_THRESHOLD_BYTES:
        # if decoding pushed the length over the threshold, raise an error
        raise InlineTooLongError(f"Inline data too large: {len(dec)} > {MAX_INLINE_THRESHOLD_BYTES}")

    return f"inline://{dec}"


def encode_inline_data(data: str) -> bytes:
    """called when loading an inline chunk"""

    if data.startswith("inline://"):
        data = data[9:]

    if data.startswith("base64:"):
        enc = base64.b64decode(data[7:])
    else:
        enc = data.encode()
    return enc


def make_object_store_key(
    version: ChunkstoreSchemaVersion, bucket_prefix: Optional[str], session_id: Optional[SessionID], token: str
) -> str:
    if version == ChunkstoreSchemaVersion.V0:
        name = token
    else:
        assert session_id, "Schema manifest versions > 0 require a session_id"
        name = f"chunks/{token}.{session_id}"

    if bucket_prefix:
        return f"{bucket_prefix}/{name}"
    else:
        return name


def make_object_store_key_from_reference_data(bucket_prefix: Optional[str], chunk_ref: ReferenceData) -> tuple[Optional[str], str]:
    """Return the object store key pointed by this ReferenceData.

    If the bucket name is available in the data, include it as the first
    element of result tuple. Otherwise, return only the object key.
    """

    assert not chunk_ref.is_inline()
    schema_version = chunk_ref.v

    if chunk_ref.is_virtual() or schema_version == ChunkstoreSchemaVersion.V0:
        if chunk_ref.uri is None:
            raise ValueError("Invalid chunk, it should have a uri")
        parsed_uri = urlparse(chunk_ref.uri)
        key = parsed_uri.path.strip("/")
        bucket = parsed_uri.netloc
        return (bucket, key)
    else:
        assert chunk_ref.is_materialized()
        assert schema_version > ChunkstoreSchemaVersion.V0

        hash = chunk_ref.hash
        assert hash, "Chunkstore schema > 0 manifests must have a hash"
        token = hash.get("token")
        assert token, "Chunkstore schema > 0 manifests must have a token"
        session = chunk_ref.sid
        assert token, "Chunkstore schema > 0 manifests must have a sid"
        return (None, make_object_store_key(version=schema_version, bucket_prefix=bucket_prefix, session_id=session, token=token))


class HashValidationError(AssertionError):
    pass


def tokenize(data: bytes, *, hasher: Callable) -> str:
    hash_obj = hasher(data)
    return hash_obj.hexdigest()


@lru_cache(maxsize=None)
def get_hasher(method):
    try:
        mod_name, func_name = method.rsplit(".", 1)
        mod = importlib.import_module(mod_name)
        return getattr(mod, func_name)
    except (ImportError, AttributeError):
        raise ValueError(f"invalid hash method {method}")


class BaseChunkstore(Chunkstore):
    """Class implementing logic for all chunkstores. It wraps an instance of
    ObjectStore which handles all the backend-specific logic around reading/writing
    bytes.
    """

    prefix: str
    schema_version: ChunkstoreSchemaVersion
    inline_threshold_bytes: int
    _known_key_cache: cachetools.LFUCache
    object_store: ObjectStore

    # TODO: consider classmethod from_object_store instead
    def __init__(
        self,
        object_store: ObjectStore,
        prefix: str,
        schema_version: ChunkstoreSchemaVersion,
        inline_threshold_bytes: int = 0,
    ):
        """
        This base class captures core chunkstore logic, but expects to be sub-classed for specific storage
        targets (s3, GCS, etc). To use this class it is required to provide an ObjectStore subclass: pull_data, put_data.
        Args:
            object_store: Underlying ObjectStore that handles reading and writing of bytes.
            prefix: a string under which all chunk keys will be placed. Must be unique for the bucket.
            schema_version: the version number for the manifest and object store key schema
            inline_threshold_bytes: Byte size below which a chunk will be stored in the metastore database. Maximum is 512.
                Values less than or equal to 0 disable inline storage.
        """
        assert prefix or schema_version == ChunkstoreSchemaVersion.V0, "schema_version > 0 requires a bucket prefix"
        self.prefix = prefix.strip("/")
        self.schema_version = schema_version
        self.object_store = object_store

        self.inline_threshold_bytes = inline_threshold_bytes
        if self.inline_threshold_bytes > MAX_INLINE_THRESHOLD_BYTES:
            raise ValueError(f"Inline chunk threshold too large, max={MAX_INLINE_THRESHOLD_BYTES} bytes")

        self._known_key_cache = cachetools.LFUCache(maxsize=KEY_CACHE_SIZE)  # tunable

    def __getstate__(self):
        return self.prefix, self.schema_version, self.inline_threshold_bytes, self.object_store

    def __setstate__(self, state):
        self.prefix, self.schema_version, self.inline_threshold_bytes, self.object_store = state
        self._known_key_cache = cachetools.LFUCache(maxsize=KEY_CACHE_SIZE)

    @property
    def bucket_name(self) -> str:
        return self.object_store.bucket_name

    @property
    def write_schema_version(self) -> ChunkstoreSchemaVersion:
        return self.schema_version

    async def ping(self):
        await self.object_store.ping()

    async def add_chunk(self, data: bytes, *, session_id: SessionID, hash_method: Optional[str] = None) -> ReferenceData:
        if isinstance(data, np.ndarray):
            # We land here if the data are not compressed by a codec. This happens for 0d arrays automatically.
            data = data.tobytes()

        if hash_method is None:
            hash_method = config.get("chunkstore.hash_method", "hashlib.sha256")

        hasher = get_hasher(hash_method)
        token = tokenize(data, hasher=hasher)
        hash = ChunkHash(method=hash_method, token=token)
        length = len(data)

        await logger.adebug("put chunk %s", token)

        inline = False
        uri: Optional[str] = None

        if length <= self.inline_threshold_bytes:
            await logger.adebug("Adding inline chunk %s", token)
            try:
                uri = decode_inline_data(data)
                inline = True
            except InlineTooLongError:
                # we failed to inline this data, so treat it like a regular chunk
                pass

        if inline is False:
            key = make_object_store_key(self.schema_version, bucket_prefix=self.prefix, session_id=session_id, token=token)

            if token not in self._known_key_cache:
                await self.object_store.put_data(data=data, key=key)
                self._known_key_cache[token] = None

            if self.schema_version == ChunkstoreSchemaVersion.V0:
                uri = self.object_store.make_uri(key)
                return ReferenceData.new_materialized_v0(uri=uri, length=len(data), hash=hash)
            elif self.schema_version == ChunkstoreSchemaVersion.V1:
                return ReferenceData.new_materialized_v1(length=len(data), hash=hash, sid=session_id)
            else:
                assert False, f"Unsupported chunkstore schema version {self.schema_version}"

        else:
            assert uri
            return ReferenceData.new_inline(for_version=self.schema_version, data=uri, length=length, hash=hash, sid=session_id)

    async def get_chunk(self, chunk_ref: ReferenceData, *, validate: bool = False) -> bytes:
        logger.debug("get_chunk %s", chunk_ref)

        if chunk_ref.is_inline():
            assert chunk_ref.uri
            # chunk is inline
            key = chunk_ref.uri
            data = encode_inline_data(chunk_ref.uri)
        else:
            # chunk is on s3
            (bucket_name, key) = make_object_store_key_from_reference_data(self.prefix, chunk_ref)
            data = await self.object_store.pull_data(
                start_byte=chunk_ref.offset, length=chunk_ref.length, key=key, bucket=bucket_name or self.bucket_name
            )

        if validate:
            # TODO should this fail for virtual chunks? We never set the hash
            if chunk_ref.hash is None:
                raise ValueError("chunk hash not set, cannot validate")
            hasher = get_hasher(chunk_ref.hash["method"])
            h = tokenize(data, hasher=hasher)
            if h != chunk_ref.hash["token"]:
                raise HashValidationError(f"hashes did not match for key: {key}")

        return data

    def __repr__(self):
        return (
            f"<{type(self).__name__}, object_store={type(self.object_store).__name__}, "
            f"bucket_name={self.bucket_name!r} "
            f"schema_version='{self.schema_version}' "
            f"prefix={self.prefix!r} "
            f"status={self.object_store.status}>"
        )
