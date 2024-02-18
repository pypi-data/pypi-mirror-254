import inspect
from dataclasses import dataclass
from typing import Callable, List


@dataclass
class SignatureLock:
    """
    Representation of a signature of Lock

    Note:
        This signature was created for give more possibilities to the user.
        For example in future version, the user can lock a function with a same signature.

    Attributes:
        is_class: If the function is a class (__call__ method)
        is_method: If the function is a method (function in a class)
        is_builtin: If the function is a builtin (like print, sum, ...)
        is_function: If the function is a function (like def, lambda, ...)
        return_annotation: Return annotation of function (def hello() -> str: ...)

        parameters: Parameters of function (def hello(a, b, c): ...)
        parameters_type: Parameters type of function (def hello(a: int, b: str, c: bool): ...)
    """

    is_class: bool
    is_method: bool
    is_builtin: bool
    is_function: bool
    return_annotation: str

    parameters: List[str]
    parameters_type: List[str]

    @classmethod
    def from_function(cls, function: Callable) -> "SignatureLock":
        """
        Create a SignatureLock from a function

        Args:
            function: Function to create signature
        """
        signature = inspect.signature(function)

        return cls(
            is_class=inspect.isclass(function),
            is_method=inspect.ismethod(function),
            is_builtin=inspect.isbuiltin(function),
            is_function=inspect.isfunction(function),
            return_annotation=f"{signature.return_annotation}",
            parameters=[f"{p.name}" for p in signature.parameters.values()],
            parameters_type=[f"{p.annotation}" for p in signature.parameters.values()],
        )
