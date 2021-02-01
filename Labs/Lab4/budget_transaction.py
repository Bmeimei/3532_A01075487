# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/27 23:28 
# File Name:        budget_transaction.py

from abc import ABC, abstractmethod
from categories import Categories
from transaction import Transaction
from rebel import Rebel
from user_type import UserType
from user_lockable_type import LockableUserType


class BudgetsTransaction(ABC):
    """
    An abstract class that support the Budgets class to handle transactions based on the specific UserType.

    It has an abstract constructor which would be extended by Budgets, and has some abstract methods that related
    to the Categories, which would be implemented by Budgets as well.

    It has many helper functions to warn and notify users after transaction.
    """

    @abstractmethod
    def __init__(self):
        """
        The abstract constructor that has the default account status, categories status and default empty list
        for containing transaction history.
        """
        self.__account_status = True
        self.__status = {
                        Categories.GAMES_ENTERTAINMENT: True,
                        Categories.CLOTHING_ACCESSORISE: True,
                        Categories.EATING_OUT: True,
                        Categories.MISCELLANEOUS: True
        }
        self.__transaction_history = []

    def process_transaction(self, transaction: Transaction, user_type: UserType) -> None:
        """
        Process a transaction, and push it into transaction history.
        This method might lock the category or account depends on the user type.
        """
        amount = transaction.get_amount()
        category = transaction.get_category_type()
        self._deduct_category_budget(category, amount)
        self.__process_exceed_budgets(user_type, category)
        self.__transaction_history.append(transaction)

    def get_transaction_history(self) -> list[Transaction]:
        """
        Returns the transaction history.

        :return: the transaction history as a list
        """
        return self.__transaction_history

    def get_account_status(self) -> bool:
        """
        Gets the boolean of the status of the account.
        True means not locked, False means banned.

        :return: A boolean that represents the account status
        """
        return self.__account_status

    def get_status(self, category: Categories) -> bool:
        """
        Gets the boolean of the lock status of a single category.
        True means not locked, False means locked.

        :param category: a category which would be searched for
        :return: A boolean that represents the lock status of category
        """
        return self.__status[category]

    def lock_category(self, category: Categories) -> None:
        """
        Locks a single category to prevent future transaction.

        :param category: a category which would be locked
        """
        self.__status[category] = False

    def ban_account(self) -> None:
        """
        Bans this budget account. All the category would be locked, and user can't do any transactions.
        """
        self.__account_status = False
        categories = [Categories.GAMES_ENTERTAINMENT, Categories.CLOTHING_ACCESSORISE,
                      Categories.EATING_OUT, Categories.MISCELLANEOUS]
        for category in categories:
            self.lock_category(category)

    def __process_exceed_budgets(self, user_type: UserType, category: Categories) -> None:
        """
        Helper function to process exceed budgets. Including:

        - Show notified
        - Show warning
        - Lock Category
        - Ban account
        """
        self.__show_notify_if_need(user_type, category)
        self.__show_warning_if_need(user_type, category)
        if isinstance(user_type, LockableUserType):
            self.__lock_category_if_need(user_type, category)
            self.__ban_account_if_need(user_type)

    def __lock_category_if_need(self, user_type: LockableUserType, category: Categories) -> None:
        """
        Locks the category after transaction if the remaining budgets below the lock threshold.
        """
        threshold = user_type.get_lock_threshold()
        if self.get_current_category(category) < self.get_origin_category(category) * (1 - threshold):
            self.lock_category(category)
            print(user_type.lock_category_message(category))

    def __ban_account_if_need(self, user_type: LockableUserType) -> None:
        """
        Bans the account. Only works for Rebel class which has over 1 locked categories.
        """
        if isinstance(user_type, Rebel) and self.numbers_of_exceed_category() > 1:
            self.ban_account()
            print(user_type.ban_account_message())

    def __show_warning_if_need(self, user_type: UserType, category: Categories) -> None:
        """
        The user would receive a warning that they are getting close
        to exceeding their assigned budget for the category in question.
        """
        threshold = user_type.get_threshold()
        if self.get_current_category(category) < self.get_origin_category(category) * (1 - threshold) \
                and not self.is_category_exceed(category):
            print(user_type.warning_message(category))

    def __show_notify_if_need(self, user_type: UserType, category: Categories) -> None:
        """
        The user receives a notification that they have exceeded their assigned budget for the category in question.
        """
        if self.is_category_exceed(category):
            print(user_type.notified(category))

    def get_current_category(self, category: Categories) -> float:
        """
        Gets the current specific category amount.
        :param category: a category which would be searched for
        :return: A float that represents the specific category cost
        """
        category_dict = self._get_current_category_dict()
        return category_dict[category]

    @abstractmethod
    def is_category_exceed(self, category: Categories) -> bool:
        """
        Checks if a specific category exceed the budget.
        :param category: the specific category
        :return: True if the category budget is under 0
        """
        pass

    @abstractmethod
    def numbers_of_exceed_category(self) -> int:
        """
        Returns the number of exceed category.

        :return: the number of exceed category as an int
        """
        pass

    @abstractmethod
    def _deduct_category_budget(self, category: Categories, amount: float) -> None:
        """
        Sets the specific category.
        The category would deduct amount.

        :param category: the specific category that would be changed
        :param amount: the process amount
        """
        pass

    @abstractmethod
    def get_origin_category(self, category: Categories) -> float:
        """
        Gets the original specific category amount from the category list.

        :param category: a category which would be searched for
        :return: A float that represents the specific category cost
        """
        pass

    @abstractmethod
    def _get_current_category_dict(self) -> dict:
        """
        Gets the current specific category dict.

        :return: current category dict
        """
        pass