# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/20 0:47 
# File Name:        transaction.py

from datetime import datetime
from user import User
from categories import Categories
from exception import check_value_is_lower_equal_than_threshold, check_type, check_string_is_empty


class Transaction:
    """
    Transactions which represent money going out of the users bank account.
    Provide the user an option to enter transaction details.

    Each transaction should contain the following information:

    - The timestamp the transaction was recorded (a nicely formatted datetime value).
    - The dollar amount (positive, non-zero number).
    - The budget category that this transaction belongs to.
      Instead of prompting the user to enter the name of the budget category,
      provide them with a list of categories and ask them to select one.
    - The name of the shop/website where the purchase took place.
    """

    _MINIMUM_TRANSACTION_AMOUNT = 0
    """
    The minimum transaction amount is 0.
    """

    def __init__(self, amount: float, user: User, category: Categories, name: str) -> None:
        """
        Constructs a transaction.
        :param amount: The dollar amount (positive, non-zero number).
        :param user: The current user.
        :param category: The budget category that this transaction belongs to.
        :param name: The name of the shop/website where the purchase took place.
        """
        check_type(amount, int, float)
        check_type(name, str)
        check_value_is_lower_equal_than_threshold(amount, 0)
        check_string_is_empty(name)
        self.timestamp = datetime.now().timestamp()
        self.amount = amount
        self.user = user
        self.category = category
        self.name = name