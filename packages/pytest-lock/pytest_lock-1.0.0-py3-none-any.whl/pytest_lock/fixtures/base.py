from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Callable, Tuple

from pytest_lock.cache import CacheLock
from pytest_lock.config import LockConfig


@dataclass
class FixtureBase(ABC):
    """
    Base class (for add mixins) for fixtures that use the lock.

    Attributes:
        config: Config of pytest-lock
        cache_system: Cache system of pytest-lock
    """

    config: LockConfig
    cache_system: CacheLock

    @abstractmethod
    def lock(self, function: Callable, arguments: Tuple[Any, ...]) -> None:
        """
        Lock a function with arguments in a cache file

        Note:
            - If lock cli argument is activated, the function will be executed and the result will be written in the cache file.
            - If lock cli argument is not activated, the function will be executed and the result will be compared with the cache file (if exists).

        Parameters:
            function (Callable): The function to lock
            arguments (Tuple[Any, ...]): The arguments of the function

        Raises:
            SkipTest: If the lock cli argument is not activated and no lock is found
            FailTest: If the lock cli argument is not activated and the function result is not equal to the lock result
            AssertionError: If the lock cli argument is not activated and the function result is not equal to the lock result
            AssertionError: If the lock cli argument is not activated and the lock is invalid (date)
        """

    @abstractmethod
    def reversed(self, function: Callable, arguments: Tuple[Any, ...]) -> None:
        """Reversed a function with reversed arguments."""
