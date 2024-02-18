from dataclasses import dataclass
from typing import Callable, Optional, Tuple

from pytest_lock.models.cache.signature import SignatureLock
from pytest_lock.typing.supports_str import SupportsStr


@dataclass
class Lock:
    """
    Representation of a lock of test

    Attributes:
        result: Result of function
        function: Name of function
        arguments: Arguments of function

        result_type: Type of result
        function_type: Type of function
        arguments_type: Type of arguments

        signature: Signature of function

        expiration_date: Expiration date of lock
    """

    result: SupportsStr  # Can be a tuple for Exception for Pickle extension
    function: str
    arguments: str

    result_type: str
    function_type: str
    arguments_type: str

    signature: SignatureLock

    expiration_date: Optional[str] = None

    @classmethod
    def from_function_and_arguments(cls, function: Callable, arguments: Tuple[SupportsStr, ...]) -> "Lock":
        """
        Create a Lock from a function and his arguments

        Args:
            function: Function to create lock
            arguments: Arguments of function to create lock

        Returns:
            Lock: Lock created from function and arguments
        """
        try:
            result = function(*arguments)
        except Exception as exception:
            result = exception

        return cls(
            result=result,
            function=function.__name__,
            arguments=arguments.__str__(),
            result_type=type(result).__name__,
            function_type=type(function).__name__,
            arguments_type=type(arguments).__name__,
            signature=SignatureLock.from_function(function),
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Lock):
            raise NotImplementedError(f"Cannot compare Lock with {type(other)}")

        conditions = (
            self.function == other.function,
            self.arguments == other.arguments,
            self.function_type == other.function_type,
            self.arguments_type == other.arguments_type,
        )

        return all(conditions)
