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
                 contains_nuts: bool,
                 variety: ToffeeVariety,
                 name: str = "Pumpkin Caramel Toffee",
                 description: str = "Fall means sneaking pumpkin flavor into just about everything, "
                                    "but especially your desserts! We LOVE this Caramel Toffee Pumpkin Candy.",
                 product_id: str = ""
                 ) -> None:
        """
        Constructs a Pumpkin Caramel Toffee.

        :param contains_nuts: a bool that represents this toffee has nuts or not
        :param variety: Toffee Variety, could be Sea Salt or Regular
        """
        self._check_input(contains_nuts, variety, name, description, product_id)
        if len(product_id) == 0:
            product_id = "C%04dH" % PumpkinCaramelToffee._generate_id
        self._increment_id()
        self._contains_nuts = contains_nuts
        self._variety = variety
        self._name = name
        self._description = description
        self._product_id = product_id

    @staticmethod
    def generate_random_candy() -> Candy:
        contains_nuts = (randint(0, 1) == 0)
        variety = ToffeeVariety.generate_random_child()
        return PumpkinCaramelToffee(contains_nuts, variety)

    @property
    def variety(self) -> ToffeeVariety:
        """
        Returns the variety of this toffee.
        """
        return self._variety

    @property
    def contains_nuts(self) -> bool:
        """
        The Pumpkin Caramel Toffee may contain traces of nuts.
        """
        return self._contains_nuts

    @property
    def lactose_free(self) -> bool:
        """
        The Pumpkin Caramel Toffee is not lactose free
        """
        return False

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
        Pumpkin Caramel Toffee is Halloween themed.
        """
        return Holiday.HALLOWEEN

    def _check_input(self,
                     contains_nuts: bool,
                     variety: ToffeeVariety,
                     name: str,
                     description: str,
                     product_id: str
                     ) -> None:
        CheckInput.check_type(contains_nuts, bool)
        CheckInput.check_type(variety, ToffeeVariety)
        CheckInput.check_all_input_type([name, description, product_id], str)