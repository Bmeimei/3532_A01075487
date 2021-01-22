# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/20 1:10 
# File Name:        rebel.py

from user_lockable_type import LockableUserType


class Rebel(LockableUserType):
    """
    The Rebel represents a user who refuses to follow any rules and believes that society
    should be broken down and restructured. They do not want to pursue "a standard education",
    "conform to the economic/capitalist foundations of society" or "get a job".
    Parents of these children are quite worried and turn to F.A.M. when they are out of options.

    • They get a warning for every transaction after exceeding 50% of a budget.
    • Gets ruthlessly notified iIf they exceed a budget category.
    • Gets locked out of conducting transactions in a budget category
      if they exceed it by 100% of the amount assigned to the budget in question.
    • If they exceed their budget in 2 or more categories then they get locked out of their account completely
    """

    def __str__(self):
        return "Rebel"