# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/24 13:22 
# File Name:        easter_bunny.py
from enums_class import Fabric, Size, Stuffing, Holiday, Colours, EasterBunnyColor
from stuffed_animal import StuffedAnimal
from check_input import CheckInput
from colourful import Colourful


class EasterBunny(StuffedAnimal, Colourful):
    """
    The Easter Bunny is made out of Linen and stuffed with Polyester Fiberfill.
    It comes in different colours
    - White, Grey, Pink and Blue and nothing else.
    """

    """
    A Number that would represents the product id.
    """
    _generate_id = 0

    def __init__(self,
                 colour: EasterBunnyColor,
                 size: Size,
                 name: str = "Easter Bunny",
                 description: str = "Imaginary rabbit said to bring gifts to children at Easter.",
                 product_id: str = ""
                 ):
        """
        Constructs a Easter Bunny.
        """
        self._check_input(colour, size, name, description, product_id)
        self._colour = colour
        self._size = size
        if len(product_id) == 0:
            product_id = "S%04dE" % EasterBunny._generate_id
        self._increment_id()
        self._name = name
        self._description = description
        self._product_id = product_id

    @property
    def colour(self) -> Colours:
        """
        Gets colour.
        """
        return self._colour

    @staticmethod
    def generate_random_animal() -> StuffedAnimal:
        colour = EasterBunnyColor.generate_random_child()
        size = Size.generate_random_child()
        return EasterBunny(colour, size)

    @property
    def stuffing(self) -> Stuffing:
        return Stuffing.POLYESTER_Fiberfill

    @property
    def size(self) -> Size:
        return self._size

    @property
    def fabric(self) -> Fabric:
        return Fabric.LINEN

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def product_id(self) -> str:
        return self._product_id

    @staticmethod
    def holiday_type() -> Holiday:
        """
        Holiday type is Easter
        """
        return Holiday.EASTER

    def _check_input(self,
                     colour: EasterBunnyColor,
                     size: Size,
                     name: str,
                     description: str,
                     product_id: str
                     ) -> None:
        CheckInput.check_type(colour, EasterBunnyColor)
        CheckInput.check_type(size, Size)
        CheckInput.check_all_input_type([name, description, product_id], str)