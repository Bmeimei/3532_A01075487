# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/21 0:09 
# File Name:        user_lockable_type.py

from user_type import UserType
from abc import ABC, abstractmethod
from budget import Budgets


class LockableUserType(UserType, ABC):
    """
    An abstract Lockable User Type inherited from UserType for Troublemaker and Rebel class to implement.
    """

    @abstractmethod
    def lock_category(self):
        pass

    @abstractmethod
    def unlock_category(self):
        pass