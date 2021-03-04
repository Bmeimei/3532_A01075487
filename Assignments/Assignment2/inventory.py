# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/23 20:47 
# File Name:        inventory.py

from santa_work_shop import SantaWorkShop
from remote_controller_spider import RemoteControllerSpider
from robot_bunny import RobotBunny
from dancing_skeleton import DancingSkeleton
from reindeer import Reindeer
from easter_bunny import EasterBunny
from pumpkin_caramel_toffee import PumpkinCaramelToffee
from candy_canes import CandyCanes
from creme_eggs import CremeEggs
from enums_class import CandyEnum, ToyEnum, StuffedAnimalEnum
from candy import Candy
from stuffed_animal import StuffedAnimal
from toy import Toy


class Inventory:
    """
    Inventory.
    """

    def __init__(self):
        """
        Constructs an Inventory.

        All the item is out of stock at the beginning.
        """
        self._toy = []
        self._stuffed_animal = []
        self._candy = []