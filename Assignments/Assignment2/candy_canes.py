# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/24 16:12 
# File Name:        candy_canes.py
from check_input import CheckInput
from candy import Candy
from enums_class import Colours, Holiday
from colourful import Colourful


class CandyCanes(Candy, Colourful):
    """
    Candy Canes are Christmas themed.
    It is lactose free and does not contain nuts.
    The stripes on the candy cane can either be Red or Green
    """

    _generate_id = 0

    _valid_colour = [Colours.RED, Colours.GREEN]

    def __init__(self,
                 colour: Colours,
                 has_nuts: bool = False,
                 has_lactose: bool = True,
                 name: str = "Candy Canes",
                 description: str = "A candy cane is a cane-shaped stick candy often associated with Christmastide, "
                                    "as well as Saint Nicholas Day. It is traditionally white with red stripes and "
                                    "flavored with peppermint, but they also come in a variety "
                                    "of other flavors and colors.",
                 product_id: str = ""
                 ) -> None:
        """
        Constructs a Candy Canes.

        :param colour: The stripes on the candy cane can either be Red or Green
        """
        self._check_input(colour, has_nuts, has_lactose, name, description, product_id)
        if len(product_id) == 0:
            product_id = "C%04dC" % CandyCanes._generate_id
        self._increment_id()
        self._stripes_colour = colour
        super().__init__(name, description, product_id, has_nuts, has_lactose)
        self.check_colour()

    @staticmethod
    def generate_random_candy() -> Candy:
        stripes_colour = Colours.get_random_candy_canes_color()
        return CandyCanes(stripes_colour)

    @staticmethod
    def holiday_type() -> Holiday:
        """
        Candy Cane is Christmas type.
        """
        return Holiday.CHRISTMAS

    @property
    def colour(self) -> Colours:
        return self._stripes_colour

    def _check_input(self,
                     stripes_colour,
                     has_nuts: bool,
                     has_lactose: bool,
                     name: str,
                     description: str,
                     product_id: str
                     ) -> None:
        CheckInput.check_type(stripes_colour, Colours)
        CheckInput.check_all_input_type([name, description, product_id], str)
        CheckInput.check_all_input_type([has_lactose, has_nuts], bool)
