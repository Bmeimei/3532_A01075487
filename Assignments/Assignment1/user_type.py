# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/20 8:51 
# File Name:        user_type.py

from abc import ABC, abstractmethod
from categories import Categories


class UserType(ABC):
    """
    An abstract class that represents the parent class for User Types \n
    This Default UserType does not include the lock out methods for budgets and account.
    In other word, this User Type is Lock-Free.
    3 Types of user class would be extended from this User class, including:

    - ANGEL
    - TROUBLE_MAKER
    - REBEL

    Among them, TROUBLE_MAKE and REBEL are Lockable Type.

    Each user type would accept the user's budget as the input, monitoring the budget
    and sending notified or warning if user exceed more than the threshold (Based on the user type)
    of a budget category.

    Basic Attributes of UserType:

    - threshold
    """

    @abstractmethod
    def __init__(self, threshold: float) -> None:
        """
        Constructs a user type.
        Since the UserType is an abstract class, this constructor can't be called.

        :param threshold: the threshold that represents the percentage of exceeding a budget category,
                          should be range from (0, 1)
        :raise TypeError if the UserType is instantiated.
        """
        self._threshold = threshold

    def warning_message(self, category: Categories) -> str:
        """
        A warning if user exceed more than amount of value of a budget.

        :param category: Category of a budget
        :return: a string of warning message
        """
        return "WARNING: Your budget category: {0} has been exceeded the threshold: {1:.0%}!"\
            .format(category, self._threshold)

    def get_threshold(self) -> float:
        """
        Gets the threshold.

        :return: threshold as a float
        """
        return self._threshold

    @staticmethod
    def notified(category: Categories) -> str:
        """
        Gets notified if user exceeds a budget category.
        :param category: Category of a budget
        :return: a string of notified message
        """
        return "NOTIFIED: The category %s has been exceed from your budgets!" % category

    @abstractmethod
    def __str__(self) -> str:
        """
        Returns a formatted string that represents the current user type.

        :return: a formatted string that represents the user type.
        """
        return "Default User Type!"