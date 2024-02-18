import pickle  # nosec
import sys
from pathlib import Path

from pytest_lock.models.cache.file import FileCache
from pytest_lock.models.cache.lock import Lock
from pytest_lock.parser_file.base import ParserFile

if sys.version_info >= (3, 12):
    from typing import override
else:
    from typing_extensions import override


class ParserFilePickle(ParserFile):
    """
    Parser for Pickle file

    Notes:
        This parser provides better quality locks than json, which is limited by its
        requirement for "SupportsStr" objects. It's important to be aware that it's
        dangerous to use the Pickle extension, as it can execute arbitrary code,
        even if theoretically there shouldn't be a problem as long as you
        don't use external Pickle objects.

    Attributes:
        encoding: Encoding of file
        protocol: Protocol of pickle file (default: pickle.HIGHEST_PROTOCOL)
    """

    def __init__(self, encoding: str = "ASCII", protocol: int = pickle.HIGHEST_PROTOCOL):
        super().__init__(encoding=encoding)
        self.protocol = protocol

    @override
    def read_file(self, path: Path) -> FileCache:
        if not path.exists():
            return FileCache(functions=[])
        # disable bandit error B301
        content = pickle.load(open(f"{path}", "rb"), encoding=self.encoding)  # nosec

        if not isinstance(content, FileCache):
            # Todo : Add test for wrong type of content file
            raise TypeError(f"FileCache expected, got {type(content)}")

        return content

    @override
    def write_file(self, path: Path, file_cache: FileCache) -> None:
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()

        return pickle.dump(file_cache, open(f"{path}", "wb"), protocol=pickle.HIGHEST_PROTOCOL)

    @override
    def transform_data(self, lock: Lock):
        # https://stackoverflow.com/questions/49715881/how-to-pickle-inherited-exceptions

        # Pickle can't serialize Exception objects, need to use __reduce__ method
        if isinstance(lock.result, Exception) or issubclass(lock.result.__class__, Exception):
            lock.result = lock.result.__reduce__()
        return lock
