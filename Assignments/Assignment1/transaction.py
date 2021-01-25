# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/20 0:47 
# File Name:        transaction.py

from datetime import datetime
from rebel import Rebel
from user import User
from categories import Categories
from exception import check_value_is_lower_equal_than_threshold, check_type, check_string_is_empty


class Transaction:
    """
    Transactions which represent money going out of the users bank account.
    Provide the user an option to enter transaction details.

    Each transaction should contain the following information:

    - timestamp: The timestamp the transaction was recorded (a nicely formatted datetime value).
    - amount: The dollar amount (positive, non-zero number).
    - categories: The budget category that this transaction belongs to.
      Instead of prompting the user to enter the name of the budget category,
      provide them with a list of categories and ask them to select one.
    - name: The name of the shop/website where the purchase took place.
    """

    _MINIMUM_TRANSACTION_AMOUNT = 0
    """
    The minimum transaction amount is 0.
    """

    def __init__(self, amount: float, user: User, category: Categories, name: str) -> None:
        """
        Processes a transaction with timestamp.

        :param amount: The dollar amount (positive, non-zero number).
        :param user: The current user.
        :param category: The budget category that this transaction belongs to.
        :param name: The name of the shop/website where the purchase took place.
        """
        check_type(amount, int, float)
        check_type(name, str)
        check_value_is_lower_equal_than_threshold(amount, self._MINIMUM_TRANSACTION_AMOUNT)
        check_string_is_empty(name)
        self._timestamp = datetime.now().timestamp()
        self._amount = amount
        self._user = user
        self._category = category
        self._name = name
        self._is_process = False
        self._status = False
        self.__process_transaction()

    def __process_transaction(self) -> None:
        """
        Helper function to process transaction.

        - if _is_process is true, means this function has already called in the constructor, avoid the future calls.
        - if the account has been banned, prevent this transaction and print banned message.
        - if the category has been locked, prevent this transaction and print locked message.
        - if the bank balance is less than amount, the process would be rejected
          and prevent subtracting the bank balance.
        - _status would become True after the transaction processes successfully.

        :raise Exception: if this function is called after constructor.
        """
        if self._is_process:
            raise Exception("This transaction has been processed!")
        self._is_process = True

        if not self._check_account_valid():
            print(self._user.get_user_type().ban_account_message() + " Transaction has been REJECTED!")
            return None

        if not self._check_category_valid():
            print(self._user.get_user_type().lock_category_message(self._category) + " Transaction has been REJECTED!")
            return None

        if self._user.bank_balance - self._amount >= 0:
            self._user.bank_balance = self._user.bank_balance - self._amount
            self._user.budgets.deduct_category_budget(self._category, self._amount)
            self.__show_notify_if_need()
            self.__show_warning_if_need()
            self._status = True
            self.__lock_category_if_need()
            self.__ban_account_if_need()
            print("Your transaction has been processed successfully!\n")
        else:
            print("Your bank balance is insufficient to afford this purchase!")

    def get_process_status(self) -> bool:
        """
        Gets the process status. True means the transaction process successful, False means it is rejected.

        :return: a boolean that represents the status of process
        """
        return self._status

    def get_category_type(self) -> Categories:
        """
        Gets the type of Category.

        :return: the transaction budget category
        """
        return self._category

    def get_timestamp(self) -> float:
        """
        Gets the timestamp of this transaction.

        :return: the timestamp of the transaction as a float
        """
        return self._timestamp

    def _check_account_valid(self) -> bool:
        """
        Checks if the budget account is valid.

        :return: True if the account is valid, False if the account is banned
        """
        return self._user.budgets.get_account_status()

    def _check_category_valid(self) -> bool:
        """
        Checks if the category is valid.
        :return: True if the account is valid, False if the account is banned
        """
        return self._user.budgets.get_status(self._category)

    def __show_warning_if_need(self) -> None:
        """
        The user would receive a warning that they are getting close
        to exceeding their assigned budget for the category in question.
        """
        user_type = self._user.get_user_type()
        threshold = user_type.get_threshold()
        budget = self._user.budgets
        if budget.get_current_category(self._category) < budget.get_origin_category(self._category) * (1 - threshold)\
                and not budget.is_category_exceed(self._category):
            print(user_type.warning_message(self._category))

    def __show_notify_if_need(self) -> None:
        """
        The user receives a notification that they have exceeded their assigned budget for the category in question.
        """
        user_type = self._user.get_user_type()
        budget = self._user.budgets
        if budget.is_category_exceed(self._category):
            print(user_type.notified(self._category))

    def __lock_category_if_need(self) -> None:
        """
        Locks the category after transaction if the remaining budgets below the lock threshold.
        """
        user_type = self._user.get_user_type()
        threshold = user_type.get_lock_threshold()
        budget = self._user.budgets
        if budget.get_current_category(self._category) < budget.get_origin_category(self._category) * (1 - threshold):
            self._user.budgets.lock_category(self._category)
            print(user_type.lock_category_message(self._category))

    def __ban_account_if_need(self) -> None:
        """
        Bans the account. Only works for Rebel class which has over 1 locked categories.
        """
        if isinstance(self._user.get_user_type(), Rebel) and self._user.budgets.numbers_of_exceed_category() > 1:
            self._user.budgets.ban_account()
            print(self._user.get_user_type().ban_account_message())

    def __str__(self) -> str:
        """
        Returns the formatted string that represents this transaction.

        :return: a formatted string of this transaction
        """
        return "Time: %s, Amount: %f, Category: %s, Institution Name: %s" % \
               (datetime.fromtimestamp(self._timestamp), self._amount, self._category, self._name)