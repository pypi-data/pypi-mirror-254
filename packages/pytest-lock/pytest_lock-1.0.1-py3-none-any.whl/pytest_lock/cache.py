import logging
from typing import Optional

from pytest_lock.config import LockConfig
from pytest_lock.models.cache.lock import Lock
from pytest_lock.parser_file.builder import ParserFileBuilder


class CacheLock:
    """
    Pytest-lock system for writing and reading cache files.

    Args:
        config: Config of pytest-lock

    Attributes:
        parser: Parser of file to use
    """

    def __init__(self, config: LockConfig):
        parser_file_builder = ParserFileBuilder()
        self.parser = parser_file_builder.build(config.extension)
        self.config = config

    def write_lock(self, lock: Lock) -> None:
        """
        Write a lock in cache file (append or update)

        Args:
            lock: Lock to write in cache file
        """
        file_cache_path = self.config.get_file_cache()
        file_cache = self.parser.read_file(file_cache_path)

        for index, other_lock in enumerate(file_cache.functions):
            if other_lock == lock:
                # Todo : Add test for double lock of same function
                logging.info(f"Lock found, modified result {other_lock.result} with {lock.result}")
                file_cache.functions[index] = lock
                break
        else:
            logging.info(f"No lock found, create a new lock with result '{lock.result}'")
            file_cache.functions.append(lock)

        # write file_cache in path
        self.parser.write_file(file_cache_path, file_cache)

    def read_lock(self, lock: Lock) -> Optional[Lock]:
        """
        Read a lock in cache file with same signature
        """
        file_cache_path = self.config.get_file_cache()
        if not file_cache_path.exists():
            return None

        file_cache = self.parser.read_file(file_cache_path)

        for index, other_lock in enumerate(file_cache.functions):
            if other_lock == lock:
                return other_lock

        return None

    def delete_lock(self):
        """Delete a cache file if existed."""
        file_cache_path = self.config.get_file_cache()

        if file_cache_path.exists():
            if not self.config.is_simulate:
                file_cache_path.unlink()
                logging.info(f"Delete cache file '{file_cache_path}'")
            else:
                logging.info(f"[Simulate] Delete cache file '{file_cache_path}'")
        else:
            logging.info(f"No cache file found at '{file_cache_path}'")
