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

    _valid_colour = []

    @property
    @abstractmethod
    def colour(self) -> Colours:
        """
        All class that implements this class must have this Colours enum property.
        """
        pass

    def check_colour(self) -> None:
        """
        Checks if the colour is valid in the child class.
        Raise error if not.

        :raise ValueError: raise if the colour is invalid.
        """
        if self.colour not in self._valid_colour:
            raise ValueError(self.colour + " is not a valid colour!")
