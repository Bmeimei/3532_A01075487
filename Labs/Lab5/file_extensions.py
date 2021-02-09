# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/8 10:45 
# File Name:        file_extensions.py

from enum import Enum, auto


class FileExtensions(Enum):
    """
    Implement a FileExtensions Enum that has 2 valid states.

    - TXT
    - JSON
    """
    TXT = auto()
    JSON = auto()