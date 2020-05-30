import pytest
from aiorequest.urls import Address, HttpUrl, HttpsUrl, Url
from tests.markers import asyncio, unit

_host: str = "9.9.9.9"
_path: str = "/api/path"

pytestmark = [unit, asyncio]


@pytest.fixture(scope="module")
async def url() -> Address:
    yield Url(_host, protocol="ftp", path=_path)


@pytest.fixture(scope="module")
async def http_url() -> Address:
    yield HttpUrl(_host, _path)


@pytest.fixture(scope="module")
async def https_url() -> Address:
    yield HttpsUrl(_host, _path)


async def test_url_with_leading_slash() -> None:
    assert await Url(_host, protocol="ftp", path="/w/r").as_str() == f"ftp://{_host}/w/r"


async def test_url_without_leading_slash() -> None:
    assert await Url(_host, protocol="ftp", path="w/r").as_str() == f"ftp://{_host}/w/r"


async def test_url_with_full_host_path() -> None:
    assert await Url(f"ftp://{_host}/w/r", protocol="ftp").as_str() == f"ftp://{_host}/w/r"


async def test_url_host(url: Address) -> None:
    assert await url.host() == _host


async def test_url_matcher(url: Address) -> None:
    assert await url.matcher() == _path


async def test_url_as_str(url: Address) -> None:
    assert await url.as_str() == f"ftp://{_host}{_path}"


async def test_http_url_host(http_url: Address) -> None:
    assert await http_url.host() == _host


async def test_http_url_matcher(http_url: Address) -> None:
    assert await http_url.matcher() == _path


async def test_http_url_as_str(http_url: Address) -> None:
    assert await http_url.as_str() == f"http://{_host}{_path}"


async def test_https_url_host(https_url: Address) -> None:
    assert await https_url.host() == _host


async def test_https_url_matcher(https_url: Address) -> None:
    assert await https_url.matcher() == _path


async def test_https_url_as_str(https_url: Address) -> None:
    assert await https_url.as_str() == f"https://{_host}{_path}"
