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

    _inventory_type = InventoryEnum.TOY

    def __init__(self,
                 name: str,
                 description: str,
                 product_id: str,
                 min_age: int,
                 has_batteries: bool,
                 ) -> None:
        """
        Constructs a toy.

        :param min_age: The minimum recommended age of the child that the toy is safe for.
        :param has_batteries: Whether the toy is battery operated or not.
        """
        super().__init__(name, description, product_id)
        self._min_age = min_age
        self._has_batteries = has_batteries

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
    def has_batteries(self) -> bool:
        """
        Returns a boolean that represents whether the toy is battery operated or not.
        """
        return self._has_batteries

    @property
    def min_age(self) -> int:
        """
        Returns an int that represents the minimum recommended age of the child that the toy is safe for.
        """
        return self._min_age
