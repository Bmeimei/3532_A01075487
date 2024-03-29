# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/20 1:09 
# File Name:        angel.py

from user_type import UserType


class Angel(UserType):
    """
    The Angel represents a user who's parents are not worried at all.
    This child has never (as far as their parents are concerned) broken a single rule.
    They already have a five-year plan in place and a roadmap which is guaranteed to get them into Harvard.
    The Angel is the child who would set up their own FAM account so they can monitor their expenses.

    • Never gets locked out of a budget category. They can continue spending money even if they exceed the budget
      in question.
    • Gets politely notified if they exceed a budget category.
    • Gets a warning if they exceed more than 90% of a budget.
    """

    __threshold = 0.90

    def __init__(self) -> None:
        super().__init__(self.__threshold)

    def __str__(self):
        return "Angle"