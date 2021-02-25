# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/24 9:58 
# File Name:        colourful.py

from abc import ABC, abstractmethod
from enums_class import Colours


class Colourful(ABC):
    """
    The interface that indicates any child class have colour property.
    """

    @property
    @abstractmethod
    def colour(self) -> Colours:
        """
        All class that implements this class must have this Colours enum property.
        """
        pass