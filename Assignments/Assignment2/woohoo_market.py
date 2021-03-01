# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/24 20:34 
# File Name:        woohoo_market.py

from menu import Menu
from inventory import Inventory


class WooHooMarket(Menu):
    """
    Woo Hoo Supermarket.
    """

    def __init__(self) -> None:
        """
        Constructs my Woo Hoo Market.
        """
        self._inventory = Inventory()

    def process_web_orders(self) -> None:
        """
        At the end of each day the store owner downloads an excel
        file of all the online orders placed that day and process them through the system.
        """
        pass

    def check_inventory(self) -> str:
        """
        This allows the cashier to check what is currently in stock and
        will also provide a status indicator for items if the stock for this item
        """
        pass