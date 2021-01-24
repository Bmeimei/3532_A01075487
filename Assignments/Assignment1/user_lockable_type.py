# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/21 0:09 
# File Name:        user_lockable_type.py

from user_type import UserType
from abc import ABC
from categories import Categories


class LockableUserType(UserType, ABC):
    """
    An abstract Lockable User Type inherited from UserType for Troublemaker and Rebel class to implement.
    Would be implemented by:

    - TROUBLEMAKER
    - REBEL
    """

    def __init__(self, threshold: float, lock_threshold: float) -> None:
        """
        Constructs a lockable user type.

        :param threshold: the threshold that represents the percentage of exceeding a budget category,
                          should be range from (0, 1)
        :param lock_threshold: the lock threshold that represents the percentage of exceeding a budget category.
        :raise TypeError if the UserType is instantiated.
        """
        super().__init__(threshold, lock_threshold)
        self._lock_threshold = lock_threshold

    def lock_category_message(self, category: Categories) -> str:
        """
        Sends a message if the category has been locked.
        :param category: A locked category
        :return: a string that tells user the category has been locked
        """
        return "Your category: {0} has been Locked since you exceed it by {1: .0%} of the amount!"\
            .format(category, self._lock_threshold)

    def get_lock_threshold(self) -> float:
        """
        Gets the lock threshold.

        :return: the lock threshold as a float
        """
        return self._lock_threshold