# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/23 21:10 
# File Name:        toy.py

from abc import ABC, abstractmethod


class Toy(ABC):
    """
    Despite that, there are some properties of each toy that all toys have in common.
    These are:

    • Whether the toy is battery operated or not.
    • The minimum recommended age of the child that the toy is safe for.
    • A name
    • A description
    • Product ID (A unique combination of letters and numbers)
    """

    @abstractmethod
    def _check_input(self, *inputs) -> None:
        """
        Checks the all inputs value and types in the constructor.
        """
        pass

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

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Returns the name of the toy as a string.
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
        Returns an unique id as a string.
        """
        pass