from typing import Dict

from pytest_lock.parser_file.base import ParserFile
from pytest_lock.parser_file.json import ParserFileJson
from pytest_lock.parser_file.pickle import ParserFilePickle


class ParserFileBuilder:
    """
    Builder for ParserFile

    Attributes:
        mapping: Mapping of extension and ParserFile
    """

    mapping: Dict[str, ParserFile]

    def __init__(self):
        self.mapping = {".json": ParserFileJson(), ".pickle": ParserFilePickle()}

    def build(self, extension: str = ".json") -> ParserFile:
        """
        Build a ParserFile from extension

        Args:
            extension: Extension of file to build ParserFile
        """
        parser_file = self.mapping.get(extension)

        if parser_file is None:
            # Todo : Add a custom exception
            # Todo : Add test for check if exception is raised with invalid extension
            raise ValueError(f"ParserFile not found for extension : '{extension}'")

        return parser_file
