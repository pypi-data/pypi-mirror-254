from typing import List

import pytest
from _pytest.config import Config
from _pytest.python import Function


def skip_test_without_lock_fixture(config: Config, items: List[Function], name_fixture) -> None:
    """
    Hook to skip tests that don't have the 'lock' fixture.

    Args:
        config: Pytest configuration object.
        items: List of tests received by pytest.
    """

    skip_marker = pytest.mark.skip(reason=f"Skipping test as it doesn't have '{name_fixture}' fixture")

    for item in items:
        conditions = (
            # Doctests don't have 'fixturenames' attributes
            isinstance(item, pytest.DoctestItem) or (name_fixture not in item.fixturenames and "lock_test" not in item.fixturenames),
            # Todo : found sollution for give argument to pytest_collection_modifyitems
            #  without collision between src/pytest_lock/plugin.py and tests/conftest.py
            # Todo : set constant for lock fixture name and add acceptation test
        )
        # Todo : remove print
        """print("-" * 30)
        print(name_fixture)
        if isinstance(item, pytest.Function) and "lock_test" in item.fixturenames:
            print(issubclass(type(item), pytest.DoctestItem) or name_fixture not in item.fixturenames)
            print("lock_test" not in item.fixturenames)
            print(issubclass(type(item), pytest.DoctestItem))
            print(isinstance(item, pytest.DoctestItem))"""

        if any(conditions):
            """print(f"Skipping test as it doesn't have '{name_fixture}' fixture")"""
            item.add_marker(skip_marker)
        """print("-" * 30)"""
