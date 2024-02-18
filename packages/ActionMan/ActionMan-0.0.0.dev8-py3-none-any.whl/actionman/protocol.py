"""Protocols defined by ActionMan."""


from typing import Protocol, runtime_checkable


@runtime_checkable
class Stringable(Protocol):
    """An object that implements the '__str__' method and thus can be converted to a string."""

    def __str__(self) -> str:
        ...
