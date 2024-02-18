"""
Init file for pytest_lock package.

- Shortened the paths of imports.
- Added __all__ variable to import all modules.
- Added __version__ variable to import version.
"""

from pathlib import Path

from pytest_lock.fixture import FixtureLock

# Classic global variables
PROJECT_PATH = Path(__file__).parents[2]
SOURCE_PATH = Path(__file__).parents[1]
APP_PATH = Path(__file__).parents[0]

__all__ = ["FixtureLock"]
__all__ += ["PROJECT_PATH", "SOURCE_PATH", "APP_PATH"]

__version__ = (0, 1, 0)
