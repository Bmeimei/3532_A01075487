# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/24 20:34 
# File Name:        woohoo_market.py
from store import Store
from inventory import Inventory


class WooHooMarket:
    """
    Woo Hoo Supermarket.

    The User Menu.
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

    def __init__(self) -> None:
        """
        Constructs my Woo Hoo Market.
        """
        self._store = Store()

    def process_web_orders(self) -> None:
        """
        At the end of each day the store owner downloads an excel
        file of all the online orders placed that day and process them through the system.
        """
        pass

    def check_inventory(self) -> None:
        """
        This allows the cashier to check what is currently in stock and
        will also provide a status indicator for items if the stock for this item
        """
        self._store.check_store_stock()


def main():
    market = WooHooMarket()
    market.check_inventory()


if __name__ == '__main__':
    main()
