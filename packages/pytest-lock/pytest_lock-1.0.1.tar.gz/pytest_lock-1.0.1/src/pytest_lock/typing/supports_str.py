""" A protocol for objects that support str() who don't exist in Python 3.12. """

from abc import abstractmethod
from typing import Protocol, runtime_checkable


@runtime_checkable
class SupportsStr(Protocol):
    """An ABC with one abstract method __str__."""

    @abstractmethod
    def __str__(self) -> str:
        ...
