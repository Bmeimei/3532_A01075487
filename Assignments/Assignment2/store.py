# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/23 20:26 
# File Name:        store.py
from order import Order, OrderProcessing
from inventory import Inventory


class Store:
    """
    Your system should contain a Store class that should be responsible for:

    • Receiving orders and maintaining its inventory
    • Getting items from a factory class if the store does not have enough stock
    • Creating the Daily Transaction Report
    """

    def __init__(self) -> None:
        """
        Constructs a store.
        """
        self._orders = []
        self._inventory = Inventory()

    def receive_orders(self):
        """
        Receiving orders and maintaining its inventory
        """
        file_name = input("Please input the order file name(Optional, Default is orders.xlsx): ")
        if len(file_name) == 0:
            file_name = "orders.xlsx"
        process_order = OrderProcessing(file_name)
        self._orders.extend(process_order.process_orders())

    def get_items_from_factory(self):
        """
        Gets items if the store does not have enough stock.
        """
        pass

    def create_daily_transaction_report(self):
        """
        Creates daily transaction report.
        """
        for order in self._orders:
            print(order)


def main():
    a = Store()
    a.receive_orders()
    a.create_daily_transaction_report()


if __name__ == '__main__':
    main()
