"""
Proxy base class for lazy loading of objects.
Can be used as base class where a persistent mutable object is required 
to implement the methods of a given interface that consumes 
an external data source.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Iterable, TypeVar, cast

T_co = TypeVar("T_co", covariant=True)


class LazyProxy(Generic[T_co], ABC):
    """A lazy proxy class that defers the loading of the proxied object until it is accessed."""

    def __init__(self) -> None:
        self.__proxied: T_co | None = None

    def __getattr__(self, attr: str) -> object:
        return getattr(self.__get_proxied__(), attr)

    def __repr__(self) -> str:
        return repr(self.__get_proxied__())

    def __str__(self) -> str:
        return str(self.__get_proxied__())

    def __dir__(self) -> Iterable[str]:
        return self.__get_proxied__().__dir__()

    def __get_proxied__(self) -> T_co:
        proxied = self.__proxied
        if proxied is not None:
            return proxied

        self.__proxied = proxied = self.__load__()
        return proxied

    def __set_proxied__(self) -> None:
        self.__proxied = self.__load__()

    def __as_proxied__(self) -> T_co:
        return cast(T_co, self)

    @abstractmethod
    def __load__(self) -> T_co: ...
