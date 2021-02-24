# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/23 22:27 
# File Name:        remote_controller_spider.py

from toy import Toy
from enum import Enum, auto
from exceptions import CheckInput
from random import uniform, randint, sample


class SpiderType(Enum):
    """
    The type of spider - This can either be a Tarantula or a Wolf Spider and nothing else.
    """
    TARANTULA = auto()
    WOLF_SPIDER = auto()

    def __str__(self) -> str:
        """
        Returns a string of name of this Spider Type
        """
        if self is SpiderType.TARANTULA:
            return "Tarantula"
        return "Wolf Spider"

    @staticmethod
    def random_spider_type() -> "SpiderType":
        """
        Generates a random spider type.
        """
        return sample(list(SpiderType), 1)[0]


class RemoteControllerSpider(Toy):
    """
    The RC Spider is the toy to get during Halloween. This toy is battery operated.
    The different varieties of spiders that are sold have the following properties:

    • Speed
    • Jump height
    • Some spiders glow in the dark, while others do not.
    • The type of spider - This can either be a Tarantula or a Wolf Spider and nothing else.
    """

    """
    A Number that would represents the product id.
    """
    __generate_id = 0

    def __init__(self, speed: float, jump_height: float, is_grow_in_dark: bool, spider_type: SpiderType) -> None:
        self._check_input(speed, jump_height, is_grow_in_dark, spider_type)
        self.__generate_id += 1
        self._speed = speed
        self._jump_height = jump_height
        self._is_grow_in_dark = is_grow_in_dark
        self._spider_type = spider_type

    def _check_input(self, speed: float, jump_height: float, is_grow_in_dark: bool, spider_type: SpiderType) -> None:
        CheckInput.check_all_input_type([speed, jump_height], int, float)
        CheckInput.check_type(spider_type, SpiderType)
        CheckInput.check_type(is_grow_in_dark, bool)
        CheckInput.check_all_input_value_is_lower_equal_than_threshold([speed, jump_height], 0)

    @staticmethod
    def generate_random_toy() -> "Toy":
        """
        Returns a rc spider with random values.

        Speed is range from (10, 20)
        Jump Height is range from (1, 3)
        """
        speed = round(uniform(10, 20), 1)
        jump_height = round(uniform(1, 3), 1)
        is_grow_in_dark = True if randint(0, 1) == 0 else False
        spider_type = SpiderType.random_spider_type()
        return RemoteControllerSpider(speed, jump_height, is_grow_in_dark, spider_type)

    @property
    def is_battery_operated(self) -> bool:
        return True

    @property
    def minimum_recommended_safe_age(self) -> int:
        return 8

    @property
    def name(self) -> str:
        return "Terrifying %s" % self._spider_type

    @property
    def description(self) -> str:
        return "Spider Man? Nope"

    @property
    def product_id(self) -> str:
        return "T%04dH" % self.__generate_id

    @property
    def speed(self) -> float:
        """
        Returns the speed of this spider as a number.
        """
        return self._speed

    @property
    def jump_height(self) -> float:
        """
        Returns the jump height of this spider as a number.
        """
        return self._jump_height

    @property
    def is_grow_in_dark(self) -> bool:
        """
        Returns a bool that represents if this spider is growing in dark or not.
        """
        return self._is_grow_in_dark

    @property
    def spider_type(self) -> SpiderType:
        """
        Returns the spider type for this spider.
        """
        return self._spider_type