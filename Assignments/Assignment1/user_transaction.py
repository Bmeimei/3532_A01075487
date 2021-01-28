# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/27 22:53 
# File Name:        user_transaction.py

from abc import ABC, abstractmethod
from user_types import UserTypes
from troublemaker import Troublemaker
from rebel import Rebel
from angel import Angel
from user_type import UserType
from user_lockable_type import LockableUserType
from budget import Budgets
from categories import Categories
from transaction import Transaction


class UserTransaction(ABC):
    """
    An abstract class that support the User class to create transactions.

    This class includes the property of budgets and everything about transactions.
    """

    @abstractmethod
    def __init__(self, budgets: Budgets, user_type: UserTypes, bank_balance: float):
        """
        The abstract constructor that has a budgets, a user type and bank balance.

        :param budgets: the budgets as the Budgets type
        :param user_type: the specific user type
        :param bank_balance: the account balance as a float,
        """
        self._budgets = budgets
        self._user_type = self.select_account_type(user_type)
        self._bank_balance = bank_balance

    def create_transaction(self, amount: float, category: Categories, name: str) -> Transaction or None:
        """
        Creates a transaction for budgets.

        :param amount: shopping amount as a float
        :param category: a specific category
        :param name: The name of the shop/website where the purchase took place.
        :return: if transaction success, return a Transaction instance. Otherwise return None.
        """
        if not self._verify_account(amount, category):
            return None
        return Transaction(amount, category, name)

    def process_and_record_transaction(self, amount: float, category: Categories, name: str) -> None:
        """
        Process a transaction. Record it into transaction list if it is not None.
        """
        transaction = self.create_transaction(amount, category, name)
        if transaction is not None:
            print("Your transaction has been processed successfully!\n")
            print(transaction)
            self._bank_balance -= transaction.get_amount()
            self.budgets.process_transaction(transaction, self._user_type)

    def get_categories_status(self, categories: Categories) -> bool:
        """
        Gets the categories status. True if it is active, False if it is locked.

        :return: categories status as a boolean
        """
        return self.budgets.get_status(categories)

    def get_account_status(self) -> bool:
        """
        Gets the boolean of the status of the account.
        True means not locked, False means banned.

        :return: A boolean that represents the account status
        """
        return self.budgets.get_account_status()

    @staticmethod
    def select_account_type(user_type: UserTypes) -> UserType or LockableUserType:
        """
        Returns a specific user type and passing the current budgets based on the input UserTypes.

        :param user_type: input UserTypes as a Enum UserTypes.
        :return: a specific user type
        """
        total_account = {
            UserTypes.TROUBLEMAKER: Troublemaker,
            UserTypes.REBEL: Rebel,
            UserTypes.ANGEL: Angel
        }
        return total_account.get(user_type)()

    @property
    def user_type(self) -> UserType or LockableUserType:
        """
        Gets user account type.

        :return: user account type
        """
        return self._user_type

    @property
    def budgets(self) -> Budgets:
        """
        Creates a property for budgets.

        :return: A formatted string that represents the budgets
        """
        return self._budgets

    @budgets.setter
    def budgets(self, budgets: Budgets) -> None:
        """
        Sets a new budget.

        :param budgets: the new budget that replaces the old one
        """
        self._budgets = budgets

    def _verify_account(self, amount: float, category: Categories) -> bool:
        """
        Helper function to verify the account status.

        :return: True if the account is valid to process transaction. False otherwise.
        """
        if not self.get_categories_status(category):
            print((self.user_type.lock_category_message(category) + " Transaction has been REJECTED!").upper())
            return False
        if not self.get_account_status():
            print((self.user_type.ban_account_message() + " Transaction has been REJECTED!").upper())
            return False
        if self._bank_balance < amount:
            print("Your bank balance is insufficient to afford this purchase!".upper())
            return False
        return True