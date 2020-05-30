"""The module provides API for Unified Resource Locator (URL) endpoints."""
from punish import AbstractStyle, abstractstyle


class Address(AbstractStyle):
    """The class represents an interface of an address."""

    @abstractstyle
    async def matcher(self) -> str:
        """Returns a path of the URL."""
        pass

    @abstractstyle
    async def host(self) -> str:
        """Returns a domain name (host)."""
        pass

    @abstractstyle
    def __str__(self) -> str:
        """Returns address as a string."""
        pass


class Url(Address):
    """The class represents regular WEB URL item."""

    def __init__(self, host: str, protocol: str, path: str = "") -> None:
        self._host = host
        self._path = path
        self._protocol = protocol

    async def matcher(self) -> str:
        return self._path

    async def host(self) -> str:
        return self._host

    def __str__(self) -> str:
        if self._host.startswith(self._protocol):
            return self._host
        return (
            f"{self._protocol}://{self._host}"
            f"/{self._path if not self._path.startswith('/') else self._path[1:]}"
        )


class HttpUrl(Address):
    """The class represents HTTP WEB URL item."""

    def __init__(self, host: str, path: str = "") -> None:
        self._http: Url = Url(host, protocol="http", path=path)

    async def matcher(self) -> str:
        return await self._http.matcher()

    async def host(self) -> str:
        return await self._http.host()

    def __str__(self) -> str:
        return str(self._http)


class HttpsUrl(Address):
    """The class represents HTTPS WEB URL item."""

    def __init__(self, host: str, path: str = "") -> None:
        self._https: Url = Url(host, protocol="https", path=path)

    async def matcher(self) -> str:
        return await self._https.matcher()

    async def host(self) -> str:
        return await self._https.host()

    def __str__(self) -> str:
        return str(self._https)
