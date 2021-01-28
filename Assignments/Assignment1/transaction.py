# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/20 0:47 
# File Name:        transaction.py

from datetime import datetime
from categories import Categories
from exception import check_value_is_lower_equal_than_threshold, check_type, check_string_is_empty
from math import ceil


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

    def __init__(self, amount: float, category: Categories, name: str) -> None:
        """
        Processes a transaction with timestamp.

        :param amount: The dollar amount (positive, non-zero number).
        :param category: The budget category that this transaction belongs to.
        :param name: The name of the shop/website where the purchase took place.
        """
        check_type(amount, int, float)
        check_type(name, str)
        check_value_is_lower_equal_than_threshold(amount, self._MINIMUM_TRANSACTION_AMOUNT)
        check_string_is_empty(name)
        self._timestamp = datetime.now().timestamp()
        self._amount = amount
        self._category = category
        self._name = name
        self._is_process = False
        self.__process_transaction()

    def __process_transaction(self) -> None:
        """
        Helper function to process transaction.

        - if _is_process is true, means this function has already called in the constructor, avoid the future calls.

        :raise Exception: if this function is called after constructor.
        """
        if self._is_process:
            raise Exception("This transaction has been processed!")
        self._is_process = True

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

    def get_amount(self) -> float:
        """
        Gets the cost amount.

        :return: the amount as a float.
        """
        return self._amount

    def __str__(self) -> str:
        """
        Returns the formatted string that represents this transaction.

        :return: a formatted string of this transaction
        """
        return "Time: %s, Amount: %f, Category: %s, Institution Name: %s" % \
               (datetime.fromtimestamp(ceil(self._timestamp)), self._amount, self._category, self._name)