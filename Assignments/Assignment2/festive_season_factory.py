# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/23 20:54 
# File Name:        festive_season_factory.py
from stuffed_animal import StuffedAnimal
from candy import Candy
from santa_work_shop import SantaWorkShop
from remote_controller_spider import RemoteControllerSpider
from robot_bunny import RobotBunny
from dancing_skeleton import DancingSkeleton
from reindeer import Reindeer
from easter_bunny import EasterBunny
from pumpkin_caramel_toffee import PumpkinCaramelToffee
from candy_canes import CandyCanes
from creme_eggs import CremeEggs
from enums_class import Holiday, InventoryEnum
from check_input import CheckInput
from item_constructor import ItemConstructor


class FestiveSeasonFactory:
    """
    This class would generates items based on the input festive season and numbers of items.
    """

    __toy_list = [SantaWorkShop, RemoteControllerSpider, RobotBunny]
    """
    Toy List.
    """

    __stuffed_animals_list = [DancingSkeleton, Reindeer, EasterBunny]
    """
    Stuffed Animals List.
    """

    __candy_list = [PumpkinCaramelToffee, CandyCanes, CremeEggs]
    """
    Candy List.
    """

    @classmethod
    def generate_items(cls, inventory_type: InventoryEnum, holiday: Holiday, number: int = 1) -> list[ItemConstructor]:
        """
        Generates a bunch of same items.

        :param inventory_type: A specific inventory type
        :param holiday: A specific holiday
        :param number: number of items
        :return: a list of items
        """
        CheckInput.check_type(inventory_type, InventoryEnum)
        if inventory_type == InventoryEnum.TOYS:
            return cls.generate_toys(holiday, number)
        if inventory_type == InventoryEnum.STUFFED_ANIMALS:
            return cls.generate_stuffed_animals(holiday, number)
        return cls.generate_candy(holiday, number)

    @classmethod
    def generate_toys(cls, holiday: Holiday, number: int = 1) -> list[ItemConstructor]:
        """
        Generates toys.

        :param holiday: A specific holiday
        :param number: number of toys
        :return: a list of toys
        """
        CheckInput.check_type(holiday, Holiday)
        CheckInput.check_type(number, int)
        CheckInput.check_value_is_lower_equal_than_threshold(number, 0)
        for toy in cls.__toy_list:
            if toy.holiday_type == holiday:
                return [toy.generate_item() for _ in range(0, number)]

    @classmethod
    def generate_stuffed_animals(cls, holiday: Holiday, number: int = 1) -> list[ItemConstructor]:
        """
        Generates stuffed animals.

        :param holiday: A specific holiday
        :param number: number of stuffed animals
        :return: a list of animals
        """
        CheckInput.check_type(holiday, Holiday)
        CheckInput.check_type(number, int)
        CheckInput.check_value_is_lower_equal_than_threshold(number, 0)
        for animal in cls.__stuffed_animals_list:
            if animal.holiday_type == holiday:
                return [animal.generate_item() for _ in range(0, number)]

    @classmethod
    def generate_candy(cls, holiday: Holiday, number: int = 1) -> list[ItemConstructor]:
        """
        Generates candy.

        :param holiday: A specific holiday
        :param number: number of stuffed animals
        :return: a list of candy
        """
        CheckInput.check_type(holiday, Holiday)
        CheckInput.check_type(number, int)
        CheckInput.check_value_is_lower_equal_than_threshold(number, 0)
        for candy in cls.__candy_list:
            if candy.holiday_type == holiday:
                return [candy.generate_item() for _ in range(0, number)]