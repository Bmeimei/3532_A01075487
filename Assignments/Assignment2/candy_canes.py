# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/24 16:12 
# File Name:        candy_canes.py
from check_input import CheckInput
from candy import Candy
from enums_class import CandyCanesColor, Holiday
from colourful import Colourful


class CandyCanes(Candy, Colourful):
    """
    Candy Canes are Christmas themed.
    It is lactose free and does not contain nuts.
    The stripes on the candy cane can either be Red or Green
    """

    _generate_id = 0

    def __init__(self,
                 stripes_colour: CandyCanesColor,
                 name: str = "Candy Canes",
                 description: str = "A candy cane is a cane-shaped stick candy often associated with Christmastide, "
                                    "as well as Saint Nicholas Day. It is traditionally white with red stripes and "
                                    "flavored with peppermint, but they also come in a variety "
                                    "of other flavors and colors.",
                 product_id: str = ""
                 ) -> None:
        """
        Constructs a Candy Canes.

        :param stripes_colour: The stripes on the candy cane can either be Red or Green
        """
        self._check_input(stripes_colour, name, description, product_id)
        if len(product_id) == 0:
            product_id = "C%04dC" % CandyCanes._generate_id
        self._increment_id()
        self._stripes_colour = stripes_colour
        self._name = name
        self._description = description
        self._product_id = product_id

    @staticmethod
    def generate_random_candy() -> Candy:
        stripes_colour = CandyCanesColor.generate_random_child()
        return CandyCanes(stripes_colour)

    @property
    def contains_nuts(self) -> bool:
        """
        It does not contain nuts.
        """
        return False

    @property
    def lactose_free(self) -> bool:
        """
        It is lactose free.
        """
        return True

    @property
    def stripes_colour(self) -> CandyCanesColor:
        """
        Gets Stripes Colour.
        """
        return self._stripes_colour

    @property
    def name(self) -> str:
        return "Candy Canes"

    @property
    def description(self) -> str:
        return "A candy cane is a cane-shaped stick candy often associated with Christmastide," \
               " as well as Saint Nicholas Day." \
               " It is traditionally white with red stripes and flavored with peppermint," \
               " but they also come in a variety of other flavors and colors."

    @property
    def product_id(self) -> str:
        return "C%04dC" % self._generate_id

    @staticmethod
    def holiday_type() -> Holiday:
        """
        Candy Cane is Christmas type.
        """
        return Holiday.CHRISTMAS

    @property
    def colour(self) -> CandyCanesColor:
        return self.stripes_colour

    def _check_input(self,
                     stripes_colour,
                     name: str,
                     description: str,
                     product_id: str
                     ) -> None:
        CheckInput.check_type(stripes_colour, CandyCanesColor)
        CheckInput.check_all_input_type([name, description, product_id], str)