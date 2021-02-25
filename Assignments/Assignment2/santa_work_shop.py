# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/23 22:27 
# File Name:        santa_work_shop.py
from enums_class import Holiday
from toy import Toy
from check_input import CheckInput
from random import uniform, randint


class Dimensions:
    """
    dimensions (width and height)
    """
    def __init__(self, width: float, height: float) -> None:
        """
        Constructs the dimensions of this Santa's Work shop as a tuple.
        The first value is width, second value is height.

        :param width: width as an int
        :param height: height as an int
        """
        CheckInput.check_all_input_type([width, height], float, int)
        CheckInput.check_all_input_value_is_lower_equal_than_threshold([width, height], 0)
        self._width = width
        self._height = height

    @property
    def width(self) -> float:
        """
        Getter for width.
        """
        return self._width

    @property
    def height(self) -> float:
        """
        Getter for height.
        """
        return self._height

    def get_dimension(self) -> tuple:
        """
        Returns the dimension of this Santa's Work shop as a tuple. The first value is width, second value is height.

        :return: A tuple represents this dimension.
        """
        return self._width, self._height

    @staticmethod
    def random_dimension() -> "Dimensions":
        """
        Returns a random dimensions, the width and height are both range from (1, 10)
        """
        width = round(uniform(1, 10), 1)
        height = round(uniform(1, 10), 1)
        return Dimensions(width, height)

    def __str__(self):
        """
        Description of this dimension.
        """
        return "Width: %d, Height: %d" % (self.width, self._height)


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

    def __init__(self, width: float, height: float, rooms_number: int) -> None:
        """
        Constructs a Santa's Work Shop.

        :param width: width as a number
        :param height: height as a number
        :param rooms_number: rooms number as an int
        """
        self._check_input(rooms_number)
        self._increment_id()
        self._dimension = Dimensions(width, height)
        self._rooms_number = rooms_number

    @property
    def holiday_type(self) -> Holiday:
        """
        Holiday Type is Christmas.
        """
        return Holiday.CHRISTMAS

    def _check_input(self, rooms_number: int) -> None:
        """
        Checks input.
        """
        CheckInput.check_type(rooms_number, int)

    @staticmethod
    def generate_random_toy() -> Toy:
        """
        Returns a santa's work shop with random dimensions and rooms number.
        Dimensions width and height are range from (1, 10)
        Rooms number are range from (1, 5)
        """
        dimensions = Dimensions.random_dimension()
        width = dimensions.get_dimension()[0]
        height = dimensions.get_dimension()[1]
        rooms_number = randint(1, 5)
        return SantaWorkShop(width, height, rooms_number)

    @property
    def is_battery_operated(self) -> bool:
        """
        Santa Work Shop is not a battery operated toy.
        """
        return False

    @property
    def minimum_recommended_safe_age(self) -> int:
        return 3

    @property
    def name(self) -> str:
        return "Santa Workshop"

    @property
    def description(self) -> str:
        return "Merry Christmas!"

    @property
    def product_id(self) -> str:
        return "T%04dC" % self._generate_id

    @property
    def dimension(self) -> Dimensions:
        """
        Returns the dimensions of this Santa's Work shop.

        :return: dimensions
        """
        return self._dimension

    @property
    def rooms_number(self) -> int:
        """
        Returns the number of rooms.

        :return: An int that represents the number of rooms.
        """
        return self._rooms_number