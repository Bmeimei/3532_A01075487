# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/24 13:22 
# File Name:        easter_bunny.py
from enums_class import Fabric, Size, Stuffing, Holiday, Colours
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

    _valid_colour = [Colours.WHITE, Colours.GREY, Colours.PINK, Colours.BLUE]

    def __init__(self,
                 colour: Colours,
                 size: Size,
                 stuffing: Stuffing = Stuffing.POLYESTER_Fiberfill,
                 fabric: Fabric = Fabric.LINEN,
                 name: str = "Easter Bunny",
                 description: str = "Imaginary rabbit said to bring gifts to children at Easter.",
                 product_id: str = ""
                 ):
        """
        Constructs a Easter Bunny.
        """
        self._check_input(colour, size, stuffing, fabric, name, description, product_id)
        self._colour = colour
        if len(product_id) == 0:
            product_id = "S%04dE" % EasterBunny._generate_id
        self._increment_id()
        super().__init__(name, description, product_id, size, stuffing, fabric)
        self.check_colour()

    @property
    def colour(self) -> Colours:
        """
        Gets colour.
        """
        return self._colour

    @staticmethod
    def generate_random_animal() -> StuffedAnimal:
        colour = Colours.get_random_easter_bunny_color()
        size = Size.generate_random_child()
        return EasterBunny(colour, size)

    @staticmethod
    def holiday_type() -> Holiday:
        """
        Holiday type is Easter
        """
        return Holiday.EASTER

    def _check_input(self,
                     colour: Colours,
                     size: Size,
                     stuffing: Stuffing,
                     fabric: Fabric,
                     name: str,
                     description: str,
                     product_id: str
                     ) -> None:
        CheckInput.check_type(colour, Colours)
        CheckInput.check_type(stuffing, Stuffing)
        CheckInput.check_type(fabric, Fabric)
        CheckInput.check_type(size, Size)
        CheckInput.check_all_input_type([name, description, product_id], str)
