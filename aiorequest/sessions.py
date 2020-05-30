"""The module contains a set of API for HTTP sessions."""
from abc import abstractmethod
from types import TracebackType
from typing import Any, AsyncContextManager, Optional, Type
import requests
from punish import AbstractStyle
from requests.auth import HTTPBasicAuth
from aiorequest.types import Credentials, OptionalAnyDict, OptionalStr
from aiorequest.responses import HttpResponse, Response, safe_response
from aiorequest.urls import Address


class Session(AbstractStyle, AsyncContextManager["Session"]):
    """The class represents abstract interfaces for an API Session."""

    @abstractmethod
    async def get(self, url: Address, **kwargs: Any) -> Response:
        """Performs ``GET`` HTTP request of a session.

        Args:
            url: url path used to perform a request
            kwargs: keyword arguments
        Returns: response element
        """
        pass

    @abstractmethod
    async def options(self, url: Address, **kwargs: Any) -> Response:
        """Performs ``OPTIONS`` HTTP request of a session.

        Args:
            url: url path used to perform a request
            kwargs: keyword arguments
        Returns: response element
        """
        pass

    @abstractmethod
    async def head(self, url: Address, **kwargs: Any) -> Response:
        """Performs ``HEAD`` HTTP request of a session.

        Args:
            url: url path used to perform a request
            kwargs: keyword arguments
        Returns: response element
        """
        pass

    @abstractmethod
    async def post(
        self,
        url: Address,
        plain: OptionalStr = None,
        as_dict: OptionalAnyDict = None,
        **kwargs: Any,
    ) -> Response:
        """Performs ``POST`` HTTP request of a session.

        Args:
            url: url path used to perform a request
            plain: requested data as a plain text
            as_dict: requested data as dictionary (json)
            kwargs: other keyword arguments
        Returns: response element
        """
        pass

    @abstractmethod
    async def put(
        self,
        url: Address,
        plain: OptionalStr = None,
        as_dict: OptionalAnyDict = None,
        **kwargs: Any,
    ) -> Response:
        """Performs ``PUT`` HTTP request of a session.

        Args:
            url: url path used to perform a request
            plain: requested data as a plain text
            as_dict: requested data as dictionary (json)
            kwargs: other keyword arguments
        Returns: response element
        """
        pass

    @abstractmethod
    async def patch(
        self,
        url: Address,
        plain: OptionalStr = None,
        as_dict: OptionalAnyDict = None,
        **kwargs: Any,
    ) -> Response:
        """Performs ``PATCH`` HTTP request of a session.

        Args:
            url: url path used to perform a request
            plain: requested data as a plain text
            as_dict: requested data as dictionary (json)
            kwargs: other keyword arguments
        Returns: response element
        """
        pass

    @abstractmethod
    async def delete(self, url: Address, **kwargs: Any) -> Response:
        """Performs ``DELETE`` HTTP request of a session.

        Args:
            url: url path used to perform a request
            kwargs: keyword arguments
        Returns: response element
        """
        pass


class HttpSession(Session):
    """The class provides interfaces for current API HTTP session."""

    def __init__(self, session: requests.Session = requests.Session()) -> None:
        self._session: requests.Session = session

    async def __aenter__(self) -> Session:
        return self

    async def get(self, url: Address, **kwargs: Any) -> Response:
        return await safe_response(HttpResponse(self._session.get(str(url), **kwargs)))

    async def options(self, url: Address, **kwargs: Any) -> Response:
        return await safe_response(HttpResponse(self._session.options(str(url), **kwargs)))

    async def head(self, url: Address, **kwargs: Any) -> Response:
        return await safe_response(HttpResponse(self._session.head(str(url), **kwargs)))

    async def post(
        self,
        url: Address,
        plain: OptionalStr = None,
        as_dict: OptionalAnyDict = None,
        **kwargs: Any,
    ) -> Response:
        return await safe_response(
            HttpResponse(self._session.post(str(url), data=plain, json=as_dict, **kwargs))
        )

    async def put(
        self,
        url: Address,
        plain: OptionalStr = None,
        as_dict: OptionalAnyDict = None,
        **kwargs: Any,
    ) -> Response:
        return await safe_response(
            HttpResponse(self._session.put(str(url), data=plain, json=as_dict, **kwargs))
        )

    async def patch(
        self,
        url: Address,
        plain: OptionalStr = None,
        as_dict: OptionalAnyDict = None,
        **kwargs: Any,
    ) -> Response:
        return await safe_response(
            HttpResponse(self._session.patch(str(url), data=plain, json=as_dict, **kwargs))
        )

    async def delete(self, url: Address, **kwargs: Any) -> Response:
        return await safe_response(HttpResponse(self._session.delete(str(url), **kwargs)))

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        self._session.close()


class LoggedHttpSession(Session):
    """The class provides logged HTTP session."""

    def __init__(
        self, credentials: Credentials, session: requests.Session = requests.Session()
    ) -> None:
        session.auth = HTTPBasicAuth(credentials.username, credentials.password)
        self._session: Session = HttpSession(session)

    async def __aenter__(self) -> Any:
        return self._session.__aenter__()

    async def get(self, url: Address, **kwargs: Any) -> Response:
        return await self._session.get(url, **kwargs)

    async def options(self, url: Address, **kwargs: Any) -> Response:
        return await self._session.options(url, **kwargs)

    async def head(self, url: Address, **kwargs: Any) -> Response:
        return await self._session.head(url, **kwargs)

    async def post(
        self,
        url: Address,
        plain: OptionalStr = None,
        as_dict: OptionalAnyDict = None,
        **kwargs: Any,
    ) -> Response:
        return await self._session.post(url, plain, as_dict, **kwargs)

    async def put(
        self,
        url: Address,
        plain: OptionalStr = None,
        as_dict: OptionalAnyDict = None,
        **kwargs: Any,
    ) -> Response:
        return await self._session.post(url, plain, as_dict, **kwargs)

    async def patch(
        self,
        url: Address,
        plain: OptionalStr = None,
        as_dict: OptionalAnyDict = None,
        **kwargs: Any,
    ) -> Response:
        return await self._session.patch(url, plain, as_dict, **kwargs)

    async def delete(self, url: Address, **kwargs: Any) -> Response:
        return await self._session.delete(url, **kwargs)

    async def __aexit__(
        self,
        exception_type: Optional[Type[BaseException]],
        exception_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        await self._session.__aexit__(exception_type, exception_value, traceback)
