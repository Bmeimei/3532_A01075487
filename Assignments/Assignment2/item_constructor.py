# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/24 11:38 
# File Name:        item_constructor.py

from abc import ABC, abstractmethod


class ItemConstructor(ABC):
    """
    An interface that contains basic methods that every item must implement.
    Including:

    - Check Constructor Input
    - Increment Unique Id
    - Generate Item
    """

    """
    Every child item must override this generate id as 0.
    """
    _generate_id = 0

    @abstractmethod
    def _check_input(self, *inputs) -> None:
        """
        Checks the all inputs value and types in the constructor.
        """
        pass

    @classmethod
    def _increment_id(cls) -> None:
        """
        Increases the generate id.

        This method would be called whenever a item has been instantiated.
        """
        cls._generate_id += 1

    @classmethod
    @abstractmethod
    def generate_item(cls) -> "ItemConstructor":
        """
        Generates an item.

        It doesn't matter what item it is, just a item is fine.
        """
        pass