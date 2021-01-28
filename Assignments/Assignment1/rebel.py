# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/20 1:10 
# File Name:        rebel.py
from Assignments.Assignment1.categories import Categories
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

    __threshold = 0.50
    __lock_threshold = 1.00

    def __init__(self) -> None:
        super().__init__(self.__threshold, self.__lock_threshold)

    def __str__(self) -> str:
        return "Rebel"

    @staticmethod
    def ban_account_message() -> str:
        """
        Tells users their account has been banned.
        :return: a string that tells user their account has been banned.
        """
        return "Your Account has been banned!".upper()

    @staticmethod
    def notified(category: Categories) -> str:
        """
        Gets ruthlessly notified if user exceeds a budget category.
        """
        return ("YOUR ACCOUNT WOULD BE LOCKED OUT IF YOU CONTINUE EXCEEDING YOUR BUDGETS!!! "
                "NOTIFIED: The category %s has been exceed from your budgets!" % category).upper()