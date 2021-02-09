# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/8 10:36 
# File Name:        file_handler.py

from file_extensions import FileExtensions
from pathlib import Path
from json import load, loads, dumps


class FileHandler:

    @staticmethod
    def load_data(path: str, file_extensions: FileExtensions) -> dict:
        """
        This method is responsible for checking the file extension and reading the file accordingly.
        This method is also responsible for raising any exceptions if they occur.

        :param path: a path of string
        :param file_extensions: a enum that represents whether TXT or JSON
        :return: a dict that represents the data
        :raise InvalidFileTypeError: if the file extensions not belong to FileExtensions type
        :raise FileNotFoundError: if the file path not exist
        """
        if not isinstance(file_extensions, FileExtensions):
            raise InvalidFileTypeError(file_extensions)
        file = Path(path)
        if not file.is_file():
            raise FileNotFoundError("There's no file names " + path + " !")
        with file.open("r", encoding="UTF-8") as file_object:
            if file_extensions == FileExtensions.JSON:
                return load(file_object)
            else:
                result = dict()
                for json_object in file_object.readlines():
                    result |= loads(json_object)
                return result

    @staticmethod
    def write_lines(path: str, lines: dict) -> None:
        """
        This method is responsible for writing the given lines to a Text file.
        The text file should be appended to and not overwritten.
        :param path: a path of string
        :param lines: a bunch of strings as a list
        """
        with open(path, "a") as file_object:
            target = dumps(lines)
            file_object.write(target + "\n")


class InvalidFileTypeError(Exception):
    """
    This exception should be raised if the user attempts to read a file that is not a .json or a .txt file
    (or in other words, if the user attempts to read a file that is not a supported by the FileExtensions enum).
    """

    def __init__(self, invalid_type) -> None:
        """
        Initialize the Error.
        """
        self.invalid_extensions = type(invalid_type)
        super().__init__("Invalid File Extensions! %s is not belongs to .json or .txt file type!"
                         % self.invalid_extensions)