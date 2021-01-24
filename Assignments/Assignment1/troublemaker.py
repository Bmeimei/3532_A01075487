# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/20 1:09 
# File Name:        troublemaker.py

from user_lockable_type import LockableUserType


class Troublemaker(LockableUserType):
    """
    The Troublemaker represents a user who often finds themselves in... well.. trouble.
    These are usually minor incidents and their parents are concerned but not worried.
    Parents usually set up a FAM account to monitor their expenses and impose light restrictions.

    • Gets a warning if they exceed more than 75% of a budget category.
    • Gets politely notified iIf they exceed a budget category.
    • Gets locked out of conducting transactions in a budget category if they exceed
      it by 120% of the amount assigned to the budget in question.
    """

    __threshold = 0.75
    __lock_threshold = 1.2

    def __init__(self) -> None:
        """
        Constructs a Troublemaker type.
        """
        super().__init__(self.__threshold, self.__lock_threshold)

    def __str__(self) -> str:
        return "Troublemaker"