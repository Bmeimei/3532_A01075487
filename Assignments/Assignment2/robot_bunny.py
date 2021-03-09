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

    def __init__(self,
                 num_sound: int,
                 colour: RobotBunnyColor,
                 min_age: int = 6,
                 has_batteries: bool = True,
                 name: str = "Fast Rabbit",
                 description: str = "This rabbit is super fast when the battery is full!",
                 product_id: str = ""
                 ) -> None:
        """
        Constructs a robot bunny.
        """
        self._check_input(num_sound, colour, has_batteries, name, description, product_id)
        if len(product_id) == 0:
            product_id = "T%04dE" % RobotBunny._generate_id
        self._increment_id()
        self._num_sound = num_sound
        self._colour = colour
        super().__init__(name, description, product_id, min_age, has_batteries)

    def _check_input(self,
                     sound_effects_number: int,
                     colour: RobotBunnyColor,
                     has_batteries: bool,
                     name: str,
                     description: str,
                     product_id: str
                     ) -> None:
        CheckInput.check_type(sound_effects_number, int)
        CheckInput.check_type(colour, RobotBunnyColor)
        CheckInput.check_type(has_batteries, bool)
        CheckInput.check_all_input_type([name, description, product_id], str)
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
    def colour(self) -> RobotBunnyColor:
        """
        Returns the colour of this robot bunny.
        """
        return self._colour

    @property
    def num_sound(self) -> int:
        """
        Returns the number of sound effects.
        """
        return self._num_sound
