"""
The Client module contains the main classes used to interact with the Arraylake service.
For asyncio interaction, use the #AsyncClient. For regular, non-async interaction, use the #Client.

**Example usage:**

```python
from arraylake import Client
client = Client()
repo = client.get_repo("my-org/my-repo")
```
"""

import re
from collections.abc import Sequence
from dataclasses import dataclass, field
from typing import Optional

from arraylake.asyn import sync
from arraylake.chunkstore import (
    Chunkstore,
    mk_chunkstore_from_bucket_config,
    mk_chunkstore_from_uri,
)
from arraylake.config import config
from arraylake.log_util import get_logger
from arraylake.metastore import HttpMetastore, HttpMetastoreConfig
from arraylake.repo import AsyncRepo, Repo
from arraylake.types import DBID, Author, Bucket
from arraylake.types import Repo as RepoModel

logger = get_logger(__name__)

_VALID_NAME = r"(\w[\w\.\-_]+)"


def _parse_org_and_repo(org_and_repo: str) -> tuple[str, str]:
    expr = f"{_VALID_NAME}/{_VALID_NAME}"
    res = re.fullmatch(expr, org_and_repo)
    if not res:
        raise ValueError(f"Not a valid repo identifier: `{org_and_repo}`. " "Should have the form `[ORG]/[REPO]`.")
    org, repo_name = res.groups()
    return org, repo_name


def _validate_org(org_name: str):
    if not re.fullmatch(_VALID_NAME, org_name):
        raise ValueError(f"Invalid org name: `{org_name}`.")


def _default_service_uri() -> str:
    return config.get("service.uri", "https://api.earthmover.io")


def _default_token() -> Optional[str]:
    return config.get("token", None)


@dataclass
class AsyncClient:
    """Asyncio Client for interacting with ArrayLake

    Args:
        service_uri (str): [Optional] The service URI to target.
        token (str): [Optional] API token for service account authentication.
    """

    service_uri: str = field(default_factory=_default_service_uri)
    token: Optional[str] = field(default_factory=_default_token, repr=False)
    auth_org: Optional[str] = None

    def __post_init__(self):
        if self.token is not None and not self.token.startswith("ema_"):
            raise ValueError("Invalid token provided. Tokens must start with ema_")
        if not self.service_uri.startswith("http"):
            raise ValueError("service uri must start with http")
        self.auth_org = self.auth_org or config.get("user.org", None)

    async def list_repos(self, org: str) -> Sequence[RepoModel]:
        """List all repositories for the specified org

        Args:
            org: Name of the org
        """

        _validate_org(org)
        mstore = HttpMetastore(HttpMetastoreConfig(self.service_uri, org, self.token, self.auth_org))
        repos = await mstore.list_databases()
        return repos

    def _init_chunkstore(self, repo_id: DBID, bucket: Optional[Bucket]) -> Chunkstore:
        inline_threshold_bytes = int(config.get("chunkstore.inline_threshold_bytes", 0))
        client_kws = config.get("s3", {})
        if bucket is None:
            s3_uri = config.get("chunkstore.uri")
            if s3_uri is None:
                raise ValueError("Chunkstore uri is None. Please set it using: `arraylake config set chunkstore.uri URI`.")
            return mk_chunkstore_from_uri(s3_uri, inline_threshold_bytes, **client_kws)
        else:
            return mk_chunkstore_from_bucket_config(bucket, repo_id, inline_threshold_bytes, **client_kws)

    async def get_repo(self, name: str, *, checkout: bool = True) -> AsyncRepo:
        """Get a repo by name

        Args:
            name: Full name of the repo (of the form [ORG]/[REPO])
            checkout: Automatically checkout the repo after instantiation.
        """

        org, repo_name = _parse_org_and_repo(name)
        mstore = HttpMetastore(HttpMetastoreConfig(self.service_uri, org, self.token, self.auth_org))

        # This is non-optimal because open_database will list_databases again
        repos = [repo for repo in await mstore.list_databases() if repo.name == repo_name]
        if len(repos) != 1:
            raise ValueError(f"Cannot find repo `{name}`.")
        repo = repos[0]

        db = await mstore.open_database(repo_name)
        cstore = self._init_chunkstore(repo.id, repo.bucket)

        user = await mstore.get_user()

        author: Author = user.as_author()
        arepo = AsyncRepo(db, cstore, name, author)
        if checkout:
            await arepo.checkout()
        return arepo

    async def get_or_create_repo(self, name: str, bucket_nickname: Optional[str] = None, *, checkout: bool = True) -> AsyncRepo:
        """Get a repo by name. Create the repo if it doesn't already exist.

        Args:
            name: Full name of the repo (of the form [ORG]/[REPO])
            bucket_nickname: the created repo will use this bucket for its chunks.
               If the repo exists, bucket_nickname is ignored.
            checkout: Automatically checkout the repo after instantiation.
               If the repo does not exist, checkout is ignored.
        """
        org, repo_name = _parse_org_and_repo(name)
        repos = [r for r in await self.list_repos(org) if r.name == repo_name]
        if repos:
            (repo,) = repos
            if bucket_nickname:
                if repo.bucket and bucket_nickname != repo.bucket.nickname:
                    raise ValueError(
                        f"""This repo exists, but the provided {bucket_nickname=} does not
                        match the configured bucket_nickname {repo.bucket.nickname!r}."""
                    )
                elif not repo.bucket:
                    raise ValueError("This repo exists, but does not have a bucket attached. Please remove the bucket_nickname argument.")
                else:
                    return await self.get_repo(name, checkout=checkout)
            return await self.get_repo(name, checkout=checkout)
        else:
            return await self.create_repo(name, bucket_nickname)

    async def create_repo(self, name: str, bucket_nickname: Optional[str] = None) -> AsyncRepo:
        """Create a new repo

        Args:
            name: Full name of the repo to create (of the form [ORG]/[REPO])
            bucket_nickname: An optional bucket to use for the chunkstore
        """

        org, repo_name = _parse_org_and_repo(name)
        mstore = HttpMetastore(HttpMetastoreConfig(self.service_uri, org, self.token, self.auth_org))
        db = await mstore.create_database(repo_name, bucket_nickname)

        repos = [repo for repo in await mstore.list_databases() if repo.name == repo_name]
        if len(repos) != 1:
            raise ValueError(f"Error creating repository `{name}`.")
        repo = repos[0]

        cstore = self._init_chunkstore(repo.id, repo.bucket)
        user = await mstore.get_user()
        author: Author = user.as_author()

        arepo = AsyncRepo(db, cstore, name, author)
        await arepo.checkout()
        return arepo

    async def delete_repo(self, name: str, *, imsure: bool = False, imreallysure: bool = False) -> None:
        """Delete a repo

        Args:
            name: Full name of the repo to delete (of the form [ORG]/[REPO])
        """

        org, repo_name = _parse_org_and_repo(name)
        mstore = HttpMetastore(HttpMetastoreConfig(self.service_uri, org, self.token, self.auth_org))
        await mstore.delete_database(repo_name, imsure=imsure, imreallysure=imreallysure)


@dataclass
class Client:
    """Client for interacting with ArrayLake.

    Args:
        service_uri (str): [Optional] The service URI to target.
        token (str): [Optional] API token for service account authentication.
    """

    service_uri: Optional[str] = None
    token: Optional[str] = field(default=None, repr=False)
    auth_org: Optional[str] = None

    def __post_init__(self):
        if self.token is None:
            self.token = config.get("token", None)
        if self.service_uri is None:
            self.service_uri = config.get("service.uri")
        self.auth_org = self.auth_org or config.get("user.org", None)

        self.aclient = AsyncClient(self.service_uri, token=self.token, auth_org=self.auth_org)

    def list_repos(self, org: str) -> Sequence[RepoModel]:
        """List all repositories for the specified org

        Args:
            org: Name of the org
        """

        repo_list = sync(self.aclient.list_repos, org)
        return repo_list

    def get_repo(self, name: str, *, checkout: bool = True) -> Repo:
        """Get a repo by name

        Args:
            name: Full name of the repo (of the form [ORG]/[REPO])
            checkout: Automatically checkout the repo after instantiation.
        """

        arepo = sync(self.aclient.get_repo, name, checkout=checkout)
        return Repo(arepo)

    def get_or_create_repo(self, name: str, bucket_nickname: Optional[str] = None, *, checkout: bool = True) -> Repo:
        """Get a repo by name. Create the repo if it doesn't already exist.

        Args:
            name: Full name of the repo (of the form [ORG]/[REPO])
            bucket_nickname: the created repo will use this bucket for its chunks.
               If the repo exists, bucket_nickname is ignored.
            checkout: Automatically checkout the repo after instantiation.
               If the repo does not exist, checkout is ignored.
        """
        arepo = sync(self.aclient.get_or_create_repo, name, bucket_nickname, checkout=checkout)
        return Repo(arepo)

    def create_repo(self, name: str, bucket_nickname: Optional[str] = None) -> Repo:
        """Create a new repo

        Args:
            name: Full name of the repo to create (of the form [ORG]/[REPO])
            bucket_nickname: An optional bucket to use for the chunkstore
        """

        arepo = sync(self.aclient.create_repo, name, bucket_nickname)
        return Repo(arepo)

    def delete_repo(self, name: str, *, imsure: bool = False, imreallysure: bool = False) -> None:
        """Delete a repo

        Args:
            name: Full name of the repo to delete (of the form [ORG]/[REPO])
        """

        return sync(self.aclient.delete_repo, name, imsure=imsure, imreallysure=imreallysure)
