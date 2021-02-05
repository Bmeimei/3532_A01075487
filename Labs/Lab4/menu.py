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

    @staticmethod
    def _showing_user_menu() -> None:
        """
        Prints the user menu.
        """
        print("Menu:\n"
              "-----------------\n"
              "1. View Budgets\n"
              "2. Record a Transaction\n"
              "3. View Transaction by Budget\n"
              "4. View Bank Account Details\n"
              "5. Log Out")

    @staticmethod
    def _showing_main_menu() -> None:
        """
        Prints the main menu.
        """
        print("---------Main Menu---------\n"
              "1. Register New User\n"
              "2. Login\n"
              "3. Exit")

    @abstractmethod
    def _showing_login_menu(self) -> None:
        """
        Prints the login menu for user.
        """
        pass

    @abstractmethod
    def _view_budgets(self) -> None:
        """
        Shows the user the current status of their budgets (locked or not)
        in addition to the amount spent, amount left, and the total amount allocated to the budget.
        """
        pass

    @abstractmethod
    def _record_transaction(self) -> None:
        """
        Takes the user to a sub-menu where they are prompted to enter the transaction details.

        :return: a recorded transaction
        """
        pass

    @abstractmethod
    def _view_transactions_by_budget(self) -> None:
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
    def _logout(self) -> None:
        """
        Log out from the current user.
        """
        pass

    @abstractmethod
    def _exit_program(self) -> None:
        """
        Terminates the process and prints the final status of users.
        """

    @abstractmethod
    def _processing_main_menu_option(self, option: str) -> None:
        """
        Processing a specific command in main menu.
        """
        pass

    @abstractmethod
    def _processing_login_menu_option(self) -> bool:
        """
        Processing a specific command in login menu.
        """
        pass

    @abstractmethod
    def _processing_user_menu_option(self, option: str) -> None:
        """
        Processing a specific command based on what menu option does User choose.
        """
        pass