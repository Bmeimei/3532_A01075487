# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/23 22:28 
# File Name:        robot_bunny.py

from toy import Toy
from enum import Enum, auto
from exceptions import CheckInput
from random import uniform, randint, sample


class Colour(Enum):
    """
    The colour - This can be either Orange, Blue, or Pink and nothing else.
    """
    ORANGE = auto()
    BLUE = auto()
    PINK = auto()

    def __str__(self):
        """
        Returns the string of colour name.
        """
        return self.name.title()

    @staticmethod
    def random_colour() -> "Colour":
        """
        Returns a random colour.
        """
        return sample(list(Colour), 1)[0]


class RobotBunny(Toy):
    """
    The Robot Bunny is the toy for toddlers and infants out there. The toy is battery operated.
    These come in different varieties as well!
    Their properties are:

    • The number of sound effects
    • The colour - This can be either Orange, Blue, or Pink and nothing else
    """

    """
    A Number that would represents the product id.
    """
    __generate_id = 0

    def __init__(self, sound_effects_number: int, colour: Colour) -> None:
        self._check_input(sound_effects_number, colour)
        self.__generate_id += 1
        self._sound_effects_number = sound_effects_number
        self._colour = colour

    def _check_input(self, sound_effects_number: int, colour: Colour) -> None:
        CheckInput.check_type(sound_effects_number, int)
        CheckInput.check_type(colour, Colour)
        CheckInput.check_value_is_lower_equal_than_threshold(sound_effects_number, 0)

    @staticmethod
    def generate_random_toy() -> "Toy":
        """
        Generates a robot bunny with random value.

        Sound Effects Number is range from (1, 4)
        """
        sound_effects_number = randint(1, 4)
        colour = Colour.random_colour()
        return RobotBunny(sound_effects_number, colour)

    @property
    def is_battery_operated(self) -> bool:
        return True

    @property
    def minimum_recommended_safe_age(self) -> int:
        return 6

    @property
    def name(self) -> str:
        return "%s Fast Rabbit" % self._colour

    @property
    def description(self) -> str:
        return "This rabbit is super fast when the battery is full!"

    @property
    def product_id(self) -> str:
        return "T%04dE" % self.__generate_id

    @property
    def colour(self) -> Colour:
        """
        Returns the colour of this robot bunny.
        """
        return self._colour

    @property
    def sound_effects_number(self) -> int:
        """
        Returns the number of sound effects.
        """
        return self._sound_effects_number