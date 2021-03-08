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

    _inventory_type = InventoryEnum.TOYS

    @staticmethod
    def inventory_type() -> InventoryEnum:
        """
        Inventory Type is Toys.
        """
        return Toy._inventory_type

    @classmethod
    def generate_item(cls) -> Item:
        """
        Generates a toy.
        """
        return cls.generate_random_toy()

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
    def min_age(self) -> int:
        """
        Returns an int that represents the minimum recommended age of the child that the toy is safe for.
        """
        pass