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

    def __init__(self):
        """

        """
        super().__init__()

    def __str__(self):
        return "Troublemaker"