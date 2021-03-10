# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/24 20:34 
# File Name:        woohoo_market.py
from Assignments.Assignment2.inventory import Inventory
from order import OrderProcessing
from store import Store


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

    def _process_web_orders(self) -> None:
        """
        At the end of each day the store owner downloads an excel
        file of all the online orders placed that day and process them through the system.
        """
        file_name = input("Please input the order file name(Optional, Default is orders.xlsx): ")
        if len(file_name) == 0:
            file_name = "orders.xlsx"
        process_order = OrderProcessing(file_name)
        for order in process_order:
            self._store.receive_order_and_process_it(order)
        print("-" * 50)
        print("Successfully Processed All the Orders! ")
        print("-" * 50)
        print()

    def _check_inventory(self) -> None:
        """
        This allows the cashier to check what is currently in stock and
        will also provide a status indicator for items if the stock for this item
        """
        print("-" * 50)
        self._store.check_store_stock()
        print("-" * 50)

    def _exit_and_print_daily_transaction_report(self) -> None:
        """
        Exits the program and print the daily transaction report.
        """
        self._store.create_daily_transaction_report()

    def execute_program(self) -> None:
        """
        Run the program -- Woo Hoo Market!
        """
        print("Welcome To WOO HOO MARKET!!")
        print("-" * 50)
        while True:
            select = input("1. Process Web Orders\n"
                           "2. Check Inventory\n"
                           "3. Exit\n"
                           "Please enter a command: ")
            if select == "1":
                self._process_web_orders()
            elif select == "2":
                self._check_inventory()
            elif select == "3":
                self._exit_and_print_daily_transaction_report()
                break
            else:
                print("%s is an INVALID Command! Please input again!" % select)
                print("-" * 50)


def main():
    market = WooHooMarket()
    market.execute_program()


if __name__ == '__main__':
    main()
