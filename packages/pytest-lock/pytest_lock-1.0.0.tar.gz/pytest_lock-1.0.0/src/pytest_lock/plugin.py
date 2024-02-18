"""
Entry point of pytest-lock plugin.

Pytest will automatically load this file when the plugin is activated.
Pytest will use the function 'pytest_addoption' to add new argument CLI.
Pytest will use the fixture 'lock' to give access to the lock feature.
"""

from pathlib import Path
from typing import List, Optional

import pytest
from _pytest.config import Config
from _pytest.python import Function
from pytest import FixtureRequest

from pytest_lock.cache import CacheLock
from pytest_lock.config import ArgumentCLI, LockConfig
from pytest_lock.fixture import FixtureLock
from pytest_lock.hooks.lock import skip_test_without_lock_fixture
from pytest_lock.models.exceptions import LockCLIException

CACHE_LOCK_PATH = ".pytest_lock"
TESTS_PATH = "tests"
EXTENSION = ".pickle"


def pytest_addoption(parser: Config):
    """Add new argument CLI to pytest."""
    parser.addoption(ArgumentCLI.LOCK, action="store_true", help="Activate lock feature, this argument make target only tests with 'lock' fixture.")  # type: ignore
    parser.addoption(ArgumentCLI.SIMULATE, action="store_true", help="Simulate lock feature")  # type: ignore
    parser.addoption(ArgumentCLI.LOCK_DATE, action="store", type=str, help="Activate lock date feature")  # type: ignore
    parser.addoption(ArgumentCLI.ONLY_SKIP, action="store_true", help="Lock only tests without lock")  # type: ignore
    parser.addoption(ArgumentCLI.CLEAN, action="store_true", help="Clean lock file")  # type: ignore


def check_cli_arguments(pytestconfig: Config) -> None:
    """
    Check if have error in cli arguments.

    Args:
        pytestconfig (Config): Pytest configuration.
    """
    is_lock = pytestconfig.getoption(ArgumentCLI.LOCK)
    is_simulate = pytestconfig.getoption(ArgumentCLI.SIMULATE)
    is_lock_date = pytestconfig.getoption(ArgumentCLI.LOCK_DATE)
    ask_only_skip = pytestconfig.getoption(ArgumentCLI.ONLY_SKIP)
    ask_clean = pytestconfig.getoption(ArgumentCLI.CLEAN)

    if not is_lock:
        if is_simulate:
            raise LockCLIException(f"Can't activate '{ArgumentCLI.SIMULATE}' mode without '{ArgumentCLI.LOCK}'")
        if is_lock_date:
            raise LockCLIException(f"Can't activate '{ArgumentCLI.LOCK_DATE}', '{is_lock_date}' mode without '{ArgumentCLI.LOCK}'")
        if ask_only_skip:
            raise LockCLIException(f"Can't activate '{ArgumentCLI.ONLY_SKIP}' mode without '{ArgumentCLI.LOCK}'")
        if ask_clean:
            raise LockCLIException(f"Can't activate '{ArgumentCLI.CLEAN}' mode without '{ArgumentCLI.LOCK}'")

    if ask_clean:
        if is_lock_date:
            raise LockCLIException(f"Can't activate '{ArgumentCLI.LOCK_DATE}', '{is_lock_date}' mode with '{ArgumentCLI.CLEAN}'")
        if ask_only_skip:
            raise LockCLIException(f"Can't activate '{ArgumentCLI.ONLY_SKIP}' mode with '{ArgumentCLI.CLEAN}'")


@pytest.fixture(scope="function")
def lock(
    pytestconfig: Config,
    request: FixtureRequest,
    tests_path: Optional[Path] = None,
    cache_path: Optional[Path] = None,
    extension: Optional[str] = None,
) -> FixtureLock:
    """
    Fixture to give access to lock feature.

    This fixture is used to give access to lock feature.
    Pytest will automatically load this fixture when the plugin is activated.

    Args:
        pytestconfig (Config): Pytest configuration.
        request (FixtureRequest): Pytest request.
        tests_path (Path, optional): Path to tests. Defaults to None.
        cache_path (Path, optional): Path to cache. Defaults to None.
        extension (str, optional): Extension of cache file. Defaults to None.

    Returns:
        FixtureLock: Lock fixture.

    """

    return _lock(
        pytestconfig=pytestconfig,
        request=request,
        tests_path=tests_path,
        cache_path=cache_path,
        extension=extension,
    )


def _lock(
    pytestconfig: Config,
    request: FixtureRequest,
    tests_path: Optional[Path] = None,
    cache_path: Optional[Path] = None,
    extension: Optional[str] = None,
) -> FixtureLock:
    """
    Fixture function accessible without use like pytest way.

    Notes:
        This way of creating the fixture is necessary, because in the tests we need to supply
        the pytesterconfig and request of the unit test and not that of the sub-test
        that launches pytest-lock. Without this manipulation, the plugin don't work
        if we want to test it. In folder tests we use _lock instead of lock, who
        can be call without use pytest way who preload lock function.

    Args:
        pytestconfig (Config): Pytest configuration.
        request (FixtureRequest): Pytest request.
        tests_path (Path, optional): Path to tests. Defaults to None.
        cache_path (Path, optional): Path to cache. Defaults to None.
        extension (str, optional): Extension of cache file. Defaults to None.

    Returns:
        FixtureLock: Lock fixture.

    """
    # Check if have error in cli arguments
    check_cli_arguments(pytestconfig)

    # Use default values if not given
    root_path = pytestconfig.rootpath
    extension = extension or EXTENSION
    tests_path = tests_path or root_path / TESTS_PATH
    cache_path = cache_path or root_path / CACHE_LOCK_PATH

    # Create configuration for lock fixture
    config = LockConfig.from_pytest_run(
        pytestconfig=pytestconfig,
        request=request,
        tests_path=tests_path,
        cache_path=cache_path,
        extension=extension,
    )

    # Create cache system
    cache_system = CacheLock(config)

    # Create lock fixture with configuration and cache system
    lock_fixture = FixtureLock(config, cache_system)

    return lock_fixture


def pytest_collection_modifyitems(config: Config, items: List[Function], name_fixture="lock") -> None:
    """
    Hook to modify tests received by pytest.

    Notes:
        This function allows you to act on tests retrieved by Pytest
        before they start running. This allows you to ignore certain
        tests, for example

    Args:
        config: Pytest configuration object.
        items: List of tests received by pytest.
        name_fixture: Name of the fixture to check.
    """
    conditions = (
        config.getoption(ArgumentCLI.LOCK),  # --lock
        config.getoption(ArgumentCLI.CLEAN),  # --lock
    )

    if any(conditions):
        skip_test_without_lock_fixture(config, items, name_fixture=name_fixture)


def pytest_configure(config: Config) -> None:
    """
    Hook to configure pytest for disable creation of cache file.

    Notes:
        When you do "pytest --lock --clean", the cache file is replace
        by a new empty file. This hook allows you to disable the creation
        of the cache file when the "--lock" argument is activated.

    Args:
        config: Pytest configuration object.
    """
    # Todo : Create a acceptation test for this hook
    # Todo : Create a test for this hook and see if pytest-cache is not created
    if config.getoption(ArgumentCLI.LOCK):
        # Disable cache file
        def fake_cache(*args, **kwargs):
            pass

        config.cache.set = fake_cache  # type: ignore
        config.cache.get = fake_cache  # type: ignore
