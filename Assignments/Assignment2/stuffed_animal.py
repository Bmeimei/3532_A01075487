# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/23 21:10 
# File Name:        stuffed_animal.py

from abc import abstractmethod

from enums_class import Stuffing, Size, Fabric, InventoryEnum
from item import Item
from item_constructor import ItemConstructor


class StuffedAnimal(Item, ItemConstructor):
    """
    All stuffed animals have the following attributes:

    • Stuffing - This can either be Polyester Fiberfill or Wool
    • Size - This can either be Small, Medium or Large
    • Fabric - This can either be Linen, Cotton or Acrylic
    • Name
    • Description
    • Product ID
    """

    @property
    def inventory_type(self) -> InventoryEnum:
        """
        Inventory Type is Stuffed Animals.
        """
        return InventoryEnum.STUFFED_ANIMALS

    def generate_item(self) -> "ItemConstructor":
        """
        Generates an animal.
        """
        return self.generate_random_animal()

    @staticmethod
    @abstractmethod
    def generate_random_animal() -> "StuffedAnimal":
        """
        Generates a stuffed animal itself with random values.
        """
        pass

    @property
    @abstractmethod
    def stuffing(self) -> Stuffing:
        """
        Returns a stuffing.

        • Polyester Fiberfill
        • Wool
        """
        pass

    @property
    @abstractmethod
    def size(self) -> Size:
        """
        Size - This can either be Small, Medium or Large

        • Small
        • Medium
        • Large
        """
        pass

    @property
    @abstractmethod
    def fabric(self) -> Fabric:
        """
        Fabric - This can either be Linen, Cotton or Acrylic

        • Linen
        • Cotton
        • Acrylic
        """
        pass