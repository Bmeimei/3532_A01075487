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

    _inventory_type = InventoryEnum.CANDY

    def __init__(self,
                 name: str,
                 description: str,
                 product_id: str,
                 has_nuts: bool,
                 has_lactose: bool):
        """
        Constructs a candy.

        :param has_nuts: boolean represents this candy has nuts or not
        :param has_lactose: boolean represents this candy has lactose or not
        """
        super().__init__(name, description, product_id)
        self._has_nuts = has_nuts
        self._has_lactose = has_lactose

    @staticmethod
    def inventory_type() -> InventoryEnum:
        """
        Inventory Type is Candy.
        """
        return Candy._inventory_type

    @classmethod
    def generate_item(cls) -> Item:
        """
        Generates a Candy. Only implemented in Candy class.
        """
        return cls.generate_random_candy()

    @staticmethod
    @abstractmethod
    def generate_random_candy() -> "Candy":
        """
        Generates a specific type of candy. It would be implemented by every sub candy classes.

        :return: A specific type of candy
        """
        pass

    @property
    def has_nuts(self) -> bool:
        """
        A flag to check if it contains any nuts.

        :return: True if it contains nuts, false not
        """
        return self._has_nuts

    @property
    def has_lactose(self) -> bool:
        """
        A flag to check if it is lactose free.

        :return: True if it is lactose free, false not
        """
        return self._has_lactose
