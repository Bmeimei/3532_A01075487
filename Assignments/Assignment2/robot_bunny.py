# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/23 22:28 
# File Name:        robot_bunny.py
from toy import Toy
from check_input import CheckInput
from random import randint
from enums_class import RobotBunnyColor, Holiday
from colourful import Colourful


class RobotBunny(Toy, Colourful):
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
    _generate_id = 0

    def __init__(self, sound_effects_number: int, colour: RobotBunnyColor) -> None:
        self._check_input(sound_effects_number, colour)
        self._increment_id()
        self._sound_effects_number = sound_effects_number
        self._colour = colour

    def _check_input(self, sound_effects_number: int, colour: RobotBunnyColor) -> None:
        CheckInput.check_type(sound_effects_number, int)
        CheckInput.check_type(colour, RobotBunnyColor)
        CheckInput.check_value_is_lower_equal_than_threshold(sound_effects_number, 0)

    @staticmethod
    def holiday_type() -> Holiday:
        """
        Holiday type is Easter.
        """
        return Holiday.EASTER

    @staticmethod
    def generate_random_toy() -> Toy:
        """
        Generates a robot bunny with random value.

        Sound Effects Number is range from (1, 4)
        """
        sound_effects_number = randint(1, 4)
        colour = RobotBunnyColor.random_colour()
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
        return "T%04dE" % self._generate_id

    @property
    def colour(self) -> RobotBunnyColor:
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