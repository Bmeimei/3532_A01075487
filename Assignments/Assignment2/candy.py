# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/23 21:10 
# File Name:        candy.py

from abc import abstractmethod
from enums_class import InventoryEnum
from item import Item
from item_constructor import ItemConstructor


class Candy(Item, ItemConstructor):
    """
    All candies have the following properties:

    • A flag to check if it contains any nuts
    • A flag to check if it is lactose free.
    • Name
    • Description
    • Product ID
    """

    @property
    def inventory_type(self) -> InventoryEnum:
        """
        Inventory Type is Candy.
        """
        return InventoryEnum.CANDY

    def generate_item(self) -> "ItemConstructor":
        """
        Generates a Candy. Only implemented in Candy class.
        """
        return self.generate_random_candy()

    @staticmethod
    @abstractmethod
    def generate_random_candy() -> "Candy":
        """
        Generates a specific type of candy. It would be implemented by every sub candy classes.

        :return: A specific type of candy
        """
        pass

    @property
    @abstractmethod
    def contains_nuts(self) -> bool:
        """
        A flag to check if it contains any nuts.

        :return: True if it contains nuts, false not
        """
        pass

    @property
    @abstractmethod
    def lactose_free(self) -> bool:
        """
        A flag to check if it is lactose free.

        :return: True if it is lactose free, false not
        """
        pass