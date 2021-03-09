# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/23 20:26 
# File Name:        store.py

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
        self._transactions = []

    def receive_orders(self):
        """
        Receives orders.
        """
        pass

    def maintain_inventory(self):
        """
        Maintains inventory.
        """
        pass

    def get_items_from_factory(self):
        """
        Gets items if the store does not have enough stock.
        """
        pass

    def create_daily_transaction_report(self):
        """
        Creates daily transaction report.
        """
        pass
