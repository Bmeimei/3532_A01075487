# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/3/3 11:43 
# File Name:        order.py

from enums_class import InventoryEnum


class Order:
    """
    Each Order contains the following:

    • Order number
    • Product ID
    • Item - The type of item (Toy, StuffedAnimal and Candy).
    • Name of the item
    • A dictionary of product details.
        These details are the rest of the attributes of the item as specified in the excel sheet EXCEPT the name
        of the holiday — Easter, Christmas or Halloween.
    • The order should also contain a reference to the appropriate Factory object that can create this item.
    """

    def __init__(self, order_number: int, product_id: str, item_type: InventoryEnum, product_details: dict) -> None:
        """
        Constructs an order.
        """
        self._order_number = order_number
        self._product_id = product_id
        self._item_type = item_type
        self._product_details = product_details