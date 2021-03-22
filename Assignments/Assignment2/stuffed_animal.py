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

    _inventory_type = InventoryEnum.STUFFED_ANIMAL

    def __init__(self,
                 name: str,
                 description: str,
                 product_id: str,
                 size: Size,
                 stuffing: Stuffing,
                 fabric: Fabric
                 ) -> None:
        """
        Constructs a stuffed animal.

        :param size: Size
        :param stuffing: Stuffing Type
        :param fabric: Fabric Type
        """
        super().__init__(name, description, product_id)
        self._size = size
        self._stuffing = stuffing
        self._fabric = fabric

    @staticmethod
    def inventory_type() -> InventoryEnum:
        """
        Inventory Type is Stuffed Animals.
        """
        return StuffedAnimal._inventory_type

    @classmethod
    def generate_item(cls) -> Item:
        """
        Generates an animal.
        """
        return cls.generate_random_animal()

    @staticmethod
    @abstractmethod
    def generate_random_animal() -> "StuffedAnimal":
        """
        Generates a stuffed animal itself with random values.
        """
        pass

    @property
    def stuffing(self) -> Stuffing:
        """
        Returns a stuffing.

        • Polyester Fiberfill
        • Wool
        """
        return self._stuffing

    @property
    def size(self) -> Size:
        """
        Size - This can either be Small, Medium or Large

        • Small
        • Medium
        • Large
        """
        return self._size

    @property
    def fabric(self) -> Fabric:
        """
        Fabric - This can either be Linen, Cotton or Acrylic

        • Linen
        • Cotton
        • Acrylic
        """
        return self._fabric
