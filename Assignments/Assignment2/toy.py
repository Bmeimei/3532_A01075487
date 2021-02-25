# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/23 21:10 
# File Name:        toy.py

from abc import abstractmethod

from enums_class import InventoryEnum
from item import Item
from item_constructor import ItemConstructor


class Toy(Item, ItemConstructor):
    """
    Despite that, there are some properties of each toy that all toys have in common.
    These are:

    • Whether the toy is battery operated or not.
    • The minimum recommended age of the child that the toy is safe for.
    • A name
    • A description
    • Product ID (A unique combination of letters and numbers)
    """

    @property
    def inventory_type(self) -> InventoryEnum:
        """
        Inventory Type is Toys.
        """
        return InventoryEnum.TOYS

    def generate_item(self) -> "ItemConstructor":
        """
        Generates a toy.
        """
        return self.generate_random_toy()

    @staticmethod
    @abstractmethod
    def generate_random_toy() -> "Toy":
        """
        Generates a toy itself with random values.
        """
        pass

    @property
    @abstractmethod
    def is_battery_operated(self) -> bool:
        """
        Returns a boolean that represents whether the toy is battery operated or not.
        """
        pass

    @property
    @abstractmethod
    def minimum_recommended_safe_age(self) -> int:
        """
        Returns an int that represents the minimum recommended age of the child that the toy is safe for.
        """
        pass