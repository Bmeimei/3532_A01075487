# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/24 11:57 
# File Name:        reindeer.py
from enums_class import Fabric, Size, Stuffing, Holiday
from stuffed_animal import StuffedAnimal
from check_input import CheckInput
from dark import GrowsInDark


class Reindeer(StuffedAnimal, GrowsInDark):
    """
    The reindeer comes with its very own personal mini sleigh and is the stuffed animal for Christmas.
    It is made out of Cotton and stuffed with Wool.

    - Has a glow in the dark nose.
    """

    """
    A Number that would represents the product id.
    """
    _generate_id = 0

    def __init__(self,
                 size: Size,
                 name: str = "Reindeer.",
                 description: str = "Reindeer is so soft and it is the best Friend of Santa.",
                 product_id: str = ""
                 ) -> None:
        """
        Constructs a Reindeer.
        """
        self._check_input(size, name, description, product_id)
        self._size = size
        if len(product_id) == 0:
            product_id = "S%04dC" % Reindeer._generate_id
        self._increment_id()
        self._name = name
        self._description = description
        self._product_id = product_id

    @staticmethod
    def generate_random_animal() -> StuffedAnimal:
        size = Size.generate_random_child()
        return Reindeer(size)

    @staticmethod
    def holiday_type() -> Holiday:
        """
        Holiday type is Christmas.
        """
        return Holiday.CHRISTMAS

    @property
    def stuffing(self) -> Stuffing:
        """
        Reindeer is made out stuffed with Wool.
        """
        return Stuffing.WOOL

    @property
    def size(self) -> Size:
        return self._size

    @property
    def fabric(self) -> Fabric:
        """
        Reindeer is made out of Cotton.
        """
        return Fabric.COTTON

    @property
    def name(self) -> str:
        return "Reindeer."

    @property
    def description(self) -> str:
        return "Reindeer is so soft and it is the best Friend of Santa."

    @property
    def product_id(self) -> str:
        return "S%04dC" % self._generate_id

    @property
    def nose(self) -> str:
        """
        Reindeer has a glow in the dark nose.
        """
        return "Dark Cute Nose"

    @property
    def is_grow_in_dark(self) -> bool:
        return True

    def _check_input(self,
                     size: Size,
                     name: str,
                     description: str,
                     product_id: str
                     ) -> None:
        CheckInput.check_type(size, Size)
        CheckInput.check_all_input_type([name, description, product_id], str)