# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/24 1:50 
# File Name:        features.py

from abc import ABC, abstractmethod
from user import User
from user_types import UserTypes
from categories import Categories
from budget import Budgets


class Features(ABC):
    """
    An abstract class that processes the basic skeleton of F.A.M.
    Including Registering User, Creating Budgets and Showing Menu
    Five functions must be implemented in F.A.M., including:

    - registering_user
    - assigning_budget_categories
    - showing_menu
    - processing_menu_option
    - execute_features
    """

    _categories_dict = {"1": Categories.GAMES_ENTERTAINMENT, "2": Categories.CLOTHING_ACCESSORISE,
                        "3": Categories.EATING_OUT, "4": Categories.MISCELLANEOUS}
    """
    The Categories Dictionary.
    """

    _user_type_dict = {"1": UserTypes.ANGEL, "2": UserTypes.TROUBLEMAKER, "3": UserTypes.REBEL}
    """
    The User Type Dictionary.
    """

    def __init__(self) -> None:
        """
        Constructs a family appointed moderator.
        Instantiates the default user, and the transaction record is an empty list for containing transactions.
        """
        self._user = User()

    def _registering_user(self) -> None:
        """
        The user (usually a parent) must register their child's financial details.
        This includes (but is not necessarily limited to):

        • The user name
        • Age
        • User Type
        • Bank Account number
        • Bank Name (optional)
        • Bank Balance
        • Their budgets
        """
        user_name = input("Please input user's name:")
        age = int(input("Please input user's age:"))
        user_type = self.__select_user_type()
        budgets = Budgets()
        bank_balance = float(input("Please input a positive bank balance:"))
        bank_name = input("Please input the bank name (Optional):")
        self._user = User(user_name, age, user_type, budgets, bank_balance, bank_name)

    def _assigning_budget_categories(self) -> None:
        """
        Each child that is being monitored is assigned the following budget categories.
        The exact value of each budget is assigned when registering the child as a user.

        • Games and Entertainment
        • Clothing and Accessories
        • Eating Out
        • Miscellaneous
        """
        games_entertainment = float(input("Please input a positive budget for Games and Entertainment:"))
        clothing_accessories = float(input("Please input a positive budget for Clothing and Accessories:"))
        eating_out = float(input("Please input a positive budget for Eating Out:"))
        miscellaneous = float(input("Please input a positive budget for miscellaneous:"))
        self._user.budgets = Budgets(games_entertainment, clothing_accessories, eating_out, miscellaneous)

    @staticmethod
    def _showing_menu() -> None:
        """
        Prints the menu.
        """
        print("1. View Budgets\n"
              "2. Record a Transaction\n"
              "3. View Transaction by Budget\n"
              "4. View Bank Account Details\n"
              "5. Exit")

    @abstractmethod
    def _processing_menu_option(self, option: str) -> None:
        """
        Processing a specific command based on what menu option does User choose.
        """
        pass

    @abstractmethod
    def execute_features(self) -> None:
        """
        The main function for executing all processes including above four functions for F.A.M.
        """
        pass

    def __select_user_type(self) -> UserTypes:
        """
        Helper function to select user type
        :return: A specific UserType
        """
        user_type_dict = self._user_type_dict
        while True:
            select = input("User Type: 1: Angel  2: Troublemaker  3: Rebel:")
            if select in user_type_dict:
                return user_type_dict[select]
            print("Invalid Command! Please Type again\n"
                  "----------------------------------")