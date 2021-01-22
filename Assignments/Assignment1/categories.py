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