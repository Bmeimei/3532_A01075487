# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/24 10:15 
# File Name:        item.py

from abc import ABC, abstractmethod
from enums_class import Holiday, InventoryEnum


class Item(ABC):
    """
    An interface that every item must implement it.

    An item must have:

    - Name
    - Description
    - Product Id

    Holiday Type
        • Easter
        • Christmas
        • Halloween

    Inventory Type
        • Toys
        • Stuffed Animals
        • Candy
    """

    def __init__(self, name: str, description: str, product_id: str):
        """
        Constructs an item.

        :param name: Name as a string.
        :param description: Description as a string.
        :param product_id: Product Id as a string.
        """
        self._name = name
        self._description = description
        self._product_id = product_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def product_id(self) -> str:
        return self._product_id

    @staticmethod
    @abstractmethod
    def holiday_type() -> Holiday:
        """
        Returns the Holiday type.

        • Easter
        • Christmas
        • Halloween
        """
        pass

    @staticmethod
    @abstractmethod
    def inventory_type() -> InventoryEnum:
        """
        Returns the Inventory type.

        • Toys
        • Stuffed Animals
        • Candy
        """
        pass

    def __str__(self) -> str:
        """
        Gets the description of this item as a string.
        """
        return "Item: %s, Product ID: %s, Name: %s" % (self.inventory_type(), self.product_id, self.name)

    def __eq__(self, other: "Item") -> bool:
        """
        Checks if two items are the same based on their product id.

        :return: True if they have the same product id, False if not
        """
        return other and self.product_id == other.product_id

    def __hash__(self) -> int:
        """
        Overrides the hash method for every item.
        """
        return hash(self.product_id)
