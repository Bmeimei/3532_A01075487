# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/23 20:26 
# File Name:        store.py
from item import Item
from order import OrderInterface, Order, InvalidOrder
from inventory import Inventory
from datetime import datetime


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
        self._inventory = Inventory.get_inventory()

    def receive_order_and_process_it(self, order: OrderInterface) -> None:
        """
        Receives one order and appends it into orders list.
        """
        try:
            if isinstance(order, Order):
                quantity = order.quantity
                factory = order.factory
                inventory_type = order.item_type
                product_id = order.product_id
                product_details = order.product_details
                product_details["product_id"] = product_id
                product_details["name"] = order.name
                if not self._inventory.check_if_item_enough(product_id, quantity):
                    item = factory.create_item(inventory_type, **product_details)
                    self.get_items_from_factory(item, quantity)
                self._inventory.export_items_by_id(product_id, quantity)

        except TypeError as e:
            order = InvalidOrder(order.order_number, e)

        finally:
            self._orders.append(order)

    def get_items_from_factory(self, item: Item, quantity: int):
        """
        Gets items if the store does not have enough stock.
        """
        self._inventory.import_items(item, quantity)

    def create_daily_transaction_report(self):
        """
        Creates daily transaction report.
        """
        date = datetime.now()
        file_name = f"DTR_{date.strftime('%d%m%Y_%H%M')}.txt"
        with open(file_name, 'w') as file_object:
            file_object.write("WOOHOO Market - DAILY TRANSACTION REPORT (DRT)\n"
                              f"{date.strftime('%d-%m-%Y  %H:%M')}\n")
            for order in self._orders:
                file_object.write(str(order))
                file_object.write("\n")

        print("Thanks For Using WOO HOOMarker! The report %s has been created!" % file_name)

    def check_store_stock(self) -> None:
        """
        Checks store stock from the inventory.
        """
        self._inventory.check_stock()
