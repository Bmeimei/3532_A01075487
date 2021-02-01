# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/21 0:39 
# File Name:        categories.py

from enum import Enum, auto


class Categories(Enum):
    """
    An Enum class that represents 4 categories of budgets in Budget class.

    - GAMES_ENTERTAINMENT
    - CLOTHING_ACCESSORISE
    - EATING_OUT
    - MISCELLANEOUS
    """
    GAMES_ENTERTAINMENT = auto()
    CLOTHING_ACCESSORISE = auto()
    EATING_OUT = auto()
    MISCELLANEOUS = auto()

    def __str__(self) -> str:
        """
        Returns the name of Enum Member

        :return: a string of Enum member
        """
        if self is self.GAMES_ENTERTAINMENT:
            return "Games and Entertainment"
        if self is self.CLOTHING_ACCESSORISE:
            return "Clothing and Accessorise"
        if self is self.EATING_OUT:
            return "Eating Out"
        return "Miscellaneous"