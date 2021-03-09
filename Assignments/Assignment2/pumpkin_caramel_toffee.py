# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/24 15:59 
# File Name:        pumpkin_caramel_toffee.py
from enums_class import Holiday, ToffeeVariety
from check_input import CheckInput
from candy import Candy
from random import randint


class PumpkinCaramelToffee(Candy):
    """
    The Pumpkin Caramel Toffee is Halloween themed and is not lactose free and may contain traces of nuts.
    It comes in two varieties — Sea Salt and Regular.
    """

    _generate_id = 0

    def __init__(self,
                 variety: ToffeeVariety,
                 has_nuts: bool,
                 has_lactose: bool = False,
                 name: str = "Pumpkin Caramel Toffee",
                 description: str = "Fall means sneaking pumpkin flavor into just about everything, "
                                    "but especially your desserts! We LOVE this Caramel Toffee Pumpkin Candy.",
                 product_id: str = ""
                 ) -> None:
        """
        Constructs a Pumpkin Caramel Toffee.

        :param has_nuts: a bool that represents this toffee has nuts or not
        :param variety: Toffee Variety, could be Sea Salt or Regular
        """
        self._check_input(has_nuts, variety, has_lactose, name, description, product_id)
        if len(product_id) == 0:
            product_id = "C%04dH" % PumpkinCaramelToffee._generate_id
        self._increment_id()
        self._variety = variety
        super().__init__(name, description, product_id, has_nuts, has_lactose)

    @staticmethod
    def generate_random_candy() -> Candy:
        contains_nuts = (randint(0, 1) == 0)
        variety = ToffeeVariety.generate_random_child()
        return PumpkinCaramelToffee(variety, contains_nuts)

    @property
    def variety(self) -> ToffeeVariety:
        """
        Returns the variety of this toffee.
        """
        return self._variety

    @staticmethod
    def holiday_type() -> Holiday:
        """
        Pumpkin Caramel Toffee is Halloween themed.
        """
        return Holiday.HALLOWEEN

    def _check_input(self,
                     contains_nuts: bool,
                     variety: ToffeeVariety,
                     has_lactose: bool,
                     name: str,
                     description: str,
                     product_id: str
                     ) -> None:
        CheckInput.check_all_input_type([contains_nuts, has_lactose], bool)
        CheckInput.check_type(variety, ToffeeVariety)
        CheckInput.check_all_input_type([name, description, product_id], str)
