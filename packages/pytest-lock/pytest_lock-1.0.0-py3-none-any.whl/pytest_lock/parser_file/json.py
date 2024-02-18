import json
import sys
from pathlib import Path

from pytest_lock.models.cache.file import FileCache
from pytest_lock.models.cache.lock import Lock
from pytest_lock.parser_file.base import ParserFile

if sys.version_info >= (3, 12):
    from typing import override
else:
    from typing_extensions import override


class ParserFileJson(ParserFile):
    """
    Parser for json file.

    Attributes:
        encoding: Encoding of file
    """

    def __init__(self, encoding: str = "utf-8"):
        super().__init__(encoding=encoding)

    @override
    def read_file(self, path: Path) -> FileCache:
        if not path.exists():
            return FileCache(functions=[])
        content = path.read_text(encoding=self.encoding)
        json_content = json.loads(content)
        return FileCache.from_json(json_content)

    @override
    def write_file(self, path: Path, file_cache: FileCache) -> None:
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()

        content = json.dumps(file_cache, indent=4, default=lambda o: o.__dict__)
        path.write_text(
            content,
            encoding=self.encoding,
        )

    @override
    def transform_data(self, lock: Lock):
        lock.result = f"{lock.result}"
        return lock
