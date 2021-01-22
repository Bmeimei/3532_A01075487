# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/20 0:13 
# File Name:        menu.py

from menu_interface import ViewMenu
from user import User


class Menu(ViewMenu):
    """
    A Menu that provides multiple options for users after they create accounts.

    - View Budgets
    - Record Transaction
    - View Transactions by Budget
    - View Bank Account Details
    """

    def __init__(self, user: User) -> None:
        """
        Constructs a menu with a user.

        :param user: The current user
        :precondition: user must be a User
        """
        self.user = user

    def view_budgets(self) -> None:
        print(self.user.budgets)

    def record_transaction(self) -> None:
        pass

    def view_transactions_by_budget(self) -> None:
        pass

    def view_bank_account_details(self) -> None:
        pass