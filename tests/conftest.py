import pytest
from aiorequest.types import AuthCredentials, Credentials
from aiorequest.responses import Response
from aiorequest.sessions import HttpSession, LoggedHttpSession, Session
from aiorequest.urls import Address, HttpUrl


@pytest.fixture(scope="session")
async def session_url() -> Address:
    yield HttpUrl(host="xkcd.com", path="info.0.json")


@pytest.fixture(scope="session")
async def credentials() -> Credentials:
    yield AuthCredentials(username="superuser", password="superpass")


@pytest.fixture(scope="session")
async def session() -> Session:
    http_session: Session
    async with HttpSession() as http_session:
        yield http_session


@pytest.fixture(scope="session")
async def logged_session(credentials: Credentials) -> Session:
    logged_http_session: Session
    async with LoggedHttpSession(
        await credentials.username, await credentials.password
    ) as logged_http_session:
        yield logged_http_session


@pytest.fixture(scope="session")
async def response(session: Session, session_url: Address) -> Response:
    yield await session.get(session_url)


@pytest.fixture(scope="session")
async def logged_response(logged_session: Session, session_url: Address) -> Response:
    yield await logged_session.get(session_url)
