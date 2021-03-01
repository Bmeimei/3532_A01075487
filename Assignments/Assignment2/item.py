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

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Returns the name as a string.
        """
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """
        Returns the description as a string.
        """
        pass

    @property
    @abstractmethod
    def product_id(self) -> str:
        """
        Returns the product id as a string.
        """
        pass

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