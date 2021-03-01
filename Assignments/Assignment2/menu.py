# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/23 20:46 
# File Name:        menu.py

from abc import ABC, abstractmethod


class Menu(ABC):
    """
    The User Menu interface
    When the program runs, it should provide a terminal menu that the store owner would have access to.
    The menu should let the cashier:

    - Process Web Orders

    At the end of each day the store owner downloads an excel file
    of all the online orders placed that day and process them through the system.

    - Check Inventory

    This allows the cashier to check what is currently in stock and
    will also provide a status indicator for items if the stock for this item
    is LOW, VERY LOW, IN STOCK, or OUT OF STOCK.

    - In Stock     - 10 or more items in stock
    - Low          - Less than 10 items
    - Very Low     - Less than 3 items
    - Out of Stock - 0 items
    """

    @abstractmethod
    def process_web_orders(self) -> None:
        """
        At the end of each day the store owner downloads an excel file
        of all the online orders placed that day and process them through the system.
        """
        pass

    @abstractmethod
    def check_inventory(self) -> str:
        """
        This allows the cashier to check what is currently in stock and
        will also provide a status indicator for items if the stock for this item
        """
        pass