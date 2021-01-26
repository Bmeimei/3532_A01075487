# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/20 0:14 
# File Name:        menu.py

from abc import ABC, abstractmethod


class ViewMenu(ABC):
    """
    An interface that must be implemented. \n
    Four methods must be implemented.

    - view_budgets
    - record_transaction
    - view_transactions_by_budget
    - view_bank_account_details
    """

    @abstractmethod
    def _view_budgets(self) -> None:
        """
        Shows the user the current status of their budgets (locked or not)
        in addition to the amount spent, amount left, and the total amount allocated to the budget.
        """
        pass

    @abstractmethod
    def record_transaction(self) -> None:
        """
        Takes the user to a sub-menu where they are prompted to enter the transaction details.

        :return: a recorded transaction
        """
        pass

    @abstractmethod
    def view_transactions_by_budget(self) -> None:
        """
        Takes the user to a sub-menu where they select their budget category
        and view all the transactions to date in that category.
        """
        pass

    @abstractmethod
    def _view_bank_account_details(self) -> None:
        """
        Prints out the bank account details of the user and all transactions
        conducted to date alongside the closing balance.
        """
        pass

    @abstractmethod
    def _exit_and_show_users_status(self) -> None:
        """
        Terminates the process and prints the final status of users.
        """