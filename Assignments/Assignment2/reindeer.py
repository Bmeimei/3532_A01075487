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
                 stuffing: Stuffing = Stuffing.WOOL,
                 fabric: Fabric = Fabric.COTTON,
                 has_grow: bool = True,
                 name: str = "Reindeer.",
                 description: str = "Reindeer is so soft and it is the best Friend of Santa.",
                 product_id: str = "") -> None:
        """
        Constructs a Reindeer.
        """
        self._check_input(size, stuffing, fabric, has_grow, name, description, product_id)
        if len(product_id) == 0:
            product_id = "S%04dC" % Reindeer._generate_id
        self._increment_id()
        self._has_grow = has_grow
        super().__init__(name, description, product_id, size, stuffing, fabric)

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
    def has_grow(self) -> bool:
        return self._has_grow

    def _check_input(self,
                     size: Size,
                     stuffing: Stuffing,
                     fabric: Fabric,
                     has_grow: bool,
                     name: str,
                     description: str,
                     product_id: str
                     ) -> None:
        CheckInput.check_type(size, Size)
        CheckInput.check_type(stuffing, Stuffing)
        CheckInput.check_type(fabric, Fabric)
        CheckInput.check_type(has_grow, bool)
        CheckInput.check_all_input_type([name, description, product_id], str)
