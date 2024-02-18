import sys
import warnings
from abc import ABC
from typing import Any, Callable, Tuple

from pytest_lock.fixtures.base import FixtureBase

if sys.version_info >= (3, 12):
    from typing import override
else:
    from typing_extensions import override


class MixinReversed(FixtureBase, ABC):
    """Mixin for lock.reversed fixture."""

    @override
    def reversed(self, function: Callable, arguments: Tuple[Any, ...]) -> None:
        warnings.warn("This method is not implemented and will be added in a future version", DeprecationWarning)
        raise NotImplementedError("This method is not implemented and will be added in a future version")
