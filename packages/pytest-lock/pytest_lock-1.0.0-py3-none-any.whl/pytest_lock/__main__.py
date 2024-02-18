"""
This module is the entry point for the pytest-lock package CLI.
"""

from pytest_lock.models.exceptions import LockException


def main():
    """Main function for the pytest-lock package."""
    raise LockException("pytest-lock don't have a cli. Please use 'pytest' instead.")


if __name__ == "__main__":
    # Todo: Add the CLI with Typer library.
    main()
