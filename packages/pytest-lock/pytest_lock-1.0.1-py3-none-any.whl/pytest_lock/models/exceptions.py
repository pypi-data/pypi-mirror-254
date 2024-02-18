class LockException(Exception):
    """Base exception for all pytest-lock exceptions."""

    pass


class LockCLIException(LockException):
    """Base exception for all pytest-lock cli exceptions."""

    pass
