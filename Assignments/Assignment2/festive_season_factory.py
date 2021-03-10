# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/23 20:54 
# File Name:        festive_season_factory.py
from abc import ABC, abstractmethod
from toy import Toy
from stuffed_animal import StuffedAnimal
from candy import Candy
from item import Item
from check_input import CheckInput
from enums_class import InventoryEnum
from santa_work_shop import SantaWorkShop
from remote_controller_spider import RemoteControllerSpider
from robot_bunny import RobotBunny
from dancing_skeleton import DancingSkeleton
from reindeer import Reindeer
from easter_bunny import EasterBunny
from pumpkin_caramel_toffee import PumpkinCaramelToffee
from candy_canes import CandyCanes
from creme_eggs import CremeEggs


class FestiveSeasonFactory(ABC):
    """
    This interfaces represents the skeleton factory of all festive season factories.
    Each factory must override these methods:

    - create_toy
    - create_stuffed_animal
    - create_candy

    It also has a default method: create_item(), which would generate an item based on the item type.
    """

    __instance = None

    @classmethod
    @abstractmethod
    def get_instance(cls) -> 'FestiveSeasonFactory':
        """
        Gets instance from the Singleton class.
        """
        pass

    @abstractmethod
    def create_toy(self, **product_details) -> Toy:
        """
        Constructs a toy.
        """
        pass

    @abstractmethod
    def create_stuffed_animal(self, **product_details) -> StuffedAnimal:
        """
        Constructs a stuffed animal.
        """
        pass

    @abstractmethod
    def create_candy(self, **product_details) -> Candy:
        """
        Constructs a candy.
        """
        pass

    def create_item(self, inventory_type: InventoryEnum, **product_details) -> Item:
        """
        Constructs an item based on the inventory type.
        """
        CheckInput.check_type(inventory_type, InventoryEnum)
        if inventory_type == InventoryEnum.TOY:
            return self.create_toy(**product_details)
        if inventory_type == InventoryEnum.STUFFED_ANIMAL:
            return self.create_stuffed_animal(**product_details)
        return self.create_candy(**product_details)


class ChristmasFactory(FestiveSeasonFactory):
    """
    Christmas Factory.
    """

    __instance = None

    def __init__(self) -> None:
        """
        Constructs a Christmas Factory by Singleton.
        """
        if ChristmasFactory.__instance is not None:
            raise Exception("The Factory already existed! Please don't create a new one!")
        ChristmasFactory.__instance = self

    @classmethod
    def get_instance(cls) -> 'FestiveSeasonFactory':
        """
        Gets instance from the Singleton class.
        """
        if cls.__instance is None:
            cls()
        return cls.__instance

    def create_toy(self, **product_details) -> Toy:
        return SantaWorkShop(**product_details)

    def create_stuffed_animal(self, **product_details) -> StuffedAnimal:
        return Reindeer(**product_details)

    def create_candy(self, **product_details) -> Candy:
        return CandyCanes(**product_details)


class HalloweenFactory(FestiveSeasonFactory):
    """
    Halloween Factory.
    """

    __instance = None

    @classmethod
    def get_instance(cls) -> 'FestiveSeasonFactory':
        if cls.__instance is None:
            cls()
        return cls.__instance

    def create_toy(self, **product_details) -> Toy:
        return RemoteControllerSpider(**product_details)

    def create_stuffed_animal(self, **product_details) -> StuffedAnimal:
        return DancingSkeleton(**product_details)

    def create_candy(self, **product_details) -> Candy:
        return PumpkinCaramelToffee(**product_details)


class EasterFactory(FestiveSeasonFactory):
    """
    Easter Factory.
    """

    __instance = None

    @classmethod
    def get_instance(cls) -> 'FestiveSeasonFactory':
        if cls.__instance is None:
            cls()
        return cls.__instance

    def create_toy(self, **product_details) -> Toy:
        return RobotBunny(**product_details)

    def create_stuffed_animal(self, **product_details) -> StuffedAnimal:
        return EasterBunny(**product_details)

    def create_candy(self, **product_details) -> Candy:
        return CremeEggs(**product_details)
