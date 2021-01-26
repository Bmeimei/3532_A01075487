# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/24 1:50 
# File Name:        features.py

from abc import ABC, abstractmethod


class Features(ABC):
    """
    An interface that shows the basic skeleton of F.A.M.
    Including Registering User, Creating Budgets and Showing Menu
    Five functions must be implemented in F.A.M., including:

    - registering_user
    - assigning_budget_categories
    - showing_menu
    - processing_menu_option
    - execute_features
    """

    @abstractmethod
    def _registering_user(self) -> None:
        """
        The user (usually a parent) must register their child's financial details.
        This includes (but is not necessarily limited to):

        • The users name
        • Age
        • User Type
        • Bank Account number
        • Bank Name
        • Bank Balance
        • Their budgets (more on this below)
        """
        pass

    @abstractmethod
    def _assigning_budget_categories(self) -> None:
        """
        Each child that is being monitored is assigned the following budget categories.
        The exact value of each budget is assigned when registering the child as a user.

        • Games and Entertainment
        • Clothing and Accessories
        • Eating Out
        • Miscellaneous
        """
        pass

    @abstractmethod
    def _showing_menu(self) -> None:
        """
        Once the user account is set up and the budgets have been created,
        the system should prompt the user with the following menu options(or a variation of the following menu).

        You could find the menu options in menu.py which is also an interface that would be implemented in F.A.M.
        """
        pass

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