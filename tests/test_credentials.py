from aiorequest import Credentials
from tests.markers import asyncio, unit

pytestmark = [unit, asyncio]


async def test_username(credentials: Credentials) -> None:
    assert await credentials.username == "superuser"


async def test_password(credentials: Credentials) -> None:
    assert await credentials.password == "superpass"


async def test_as_string(credentials: Credentials) -> None:
    assert (
        await credentials.as_str() == "AuthCredentials(username='superuser', password='superpass')"
    )
