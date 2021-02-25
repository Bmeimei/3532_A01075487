# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/24 10:07 
# File Name:        dark.py

from abc import ABC, abstractmethod


class GrowsInDark(ABC):
    """
    An interface that indicates this class is grows in dark or not.
    """

    @property
    @abstractmethod
    def is_grow_in_dark(self) -> bool:
        """
        Returns a bool that represents if this class is growing in dark or not.
        """
        pass