# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/23 22:27 
# File Name:        santa_work_shop.py
from enums_class import Holiday
from toy import Toy
from check_input import CheckInput
from random import uniform, randint


class SantaWorkShop(Toy):
    """
    The premium Christmas present, this is not a battery operated toy.
    The doll house comes in different varieties. They can vary in:

    • dimensions (width and height)
    • The number of rooms
    """

    """
    A Number that would represents the product id.
    """
    _generate_id = 0

    def __init__(self, dimensions: float, rooms_number: int,
                 min_age: int = 5,
                 name: str = "Santa Workshop",
                 description: str = "Merry Christmas!",
                 product_id: str = ""
                 ) -> None:
        """
        Constructs a Santa's Work Shop.

        :param rooms_number: rooms number as an int
        """
        self._check_input(rooms_number, dimensions, min_age, name, description, product_id)
        if len(product_id) == 0:
            product_id = "T%04dC" % SantaWorkShop._generate_id
        self._increment_id()
        self._dimensions = dimensions
        self._rooms_number = rooms_number
        self._min_age = min_age
        self._name = name
        self._description = description
        self._product_id = product_id

    @staticmethod
    def holiday_type() -> Holiday:
        """
        Holiday Type is Christmas.
        """
        return Holiday.CHRISTMAS

    def _check_input(self,
                     rooms_number: int,
                     dimensions: float,
                     min_age: int,
                     name: str,
                     description: str,
                     product_id: str) -> None:
        """
        Checks input.
        """
        CheckInput.check_all_input_type([rooms_number, min_age], int)
        CheckInput.check_type(dimensions, int, float)
        CheckInput.check_all_input_value_is_lower_equal_than_threshold([rooms_number, dimensions, min_age], 0)
        CheckInput.check_all_input_type([description, product_id, name], str)

    @staticmethod
    def generate_random_toy() -> Toy:
        """
        Returns a santa's work shop with random dimensions and rooms number.
        Dimensions width and height are range from (5, 100)
        Rooms number are range from (1, 5)
        """
        dimensions = round(uniform(5, 100), 2)
        rooms_number = randint(1, 5)
        return SantaWorkShop(dimensions, rooms_number)

    @property
    def is_battery_operated(self) -> bool:
        """
        Santa Work Shop is not a battery operated toy.
        """
        return False

    @property
    def min_age(self) -> int:
        return self._min_age

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def product_id(self) -> str:
        return self._product_id

    @property
    def dimension(self) -> float:
        """
        Returns the dimensions of this Santa's Work shop.

        :return: dimensions
        """
        return self._dimensions

    @property
    def rooms_number(self) -> int:
        """
        Returns the number of rooms.

        :return: An int that represents the number of rooms.
        """
        return self._rooms_number