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
        """
        Shows the user the current status of their budgets (locked or not)
        in addition to the amount spent, amount left, and the total amount allocated to the budget.
        """
        print(self.user.budgets)

    def record_transaction(self) -> None:
        """
        Takes the user to a sub-menu where they are prompted to enter the transaction details.
        """
        pass

    def view_transactions_by_budget(self) -> None:
        """
        Takes the user to a sub-menu where they select their budget category
        and view all the transactions to date in that category.
        """
        pass

    def view_bank_account_details(self) -> None:
        """
        Prints out the bank account details of the user and all transactions
        conducted to date alongside the closing balance.
        """
        pass