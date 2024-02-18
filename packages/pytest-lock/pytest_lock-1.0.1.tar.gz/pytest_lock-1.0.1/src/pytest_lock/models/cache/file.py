from dataclasses import dataclass
from typing import List

from pytest_lock.models.cache.lock import Lock
from pytest_lock.models.cache.signature import SignatureLock


@dataclass
class FileCache:
    """
    Representation of a cache file.

    Attributes:
        functions: List of functions in the cache file
    """

    functions: List[Lock]

    @classmethod
    def from_json(cls, json: dict):
        """
        Create a FileCache from json

        Args:
            json: Json of cache file
        """
        functions = [Lock(**function) for function in json["functions"]]

        for index, lock in enumerate(functions):
            lock.signature = SignatureLock(**json["functions"][index]["signature"])

        return cls(functions=functions)
