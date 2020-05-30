"""The module provides API for credentials."""
from abc import abstractmethod
from typing import Any, Dict, Optional, Union
from punish import AbstractStyle

AnyDict = Dict[Any, Any]
OptionalStr = Optional[str]
OptionalAnyDict = Optional[AnyDict]
AnyUnionDict = Union[AnyDict, Any]


class Credentials(AbstractStyle):
    """The class represents abstraction for credentials."""

    @property
    @abstractmethod
    async def username(self) -> str:
        """Returns a username."""
        pass

    @property
    @abstractmethod
    async def password(self) -> str:
        """Returns a password."""
        pass

    @abstractmethod
    async def as_str(self) -> str:
        """Returns credentials string representation."""
        pass


class AuthCredentials(Credentials):
    """The class represents authorization credentials."""

    def __init__(self, username: str, password: str) -> None:
        self._username: str = username
        self._password: str = password

    @property
    async def username(self) -> str:
        """Returns auth username."""
        return self._username

    @property
    async def password(self) -> str:
        """Returns auth password."""
        return self._password

    async def as_str(self) -> str:
        """Returns auth credentials string representation."""
        return (
            f"{self.__class__.__name__}"
            f"(username='{await self.username}', password='{await self.password}')"
        )
