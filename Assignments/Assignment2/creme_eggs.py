# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/24 16:30 
# File Name:        creme_eggs.py
from enums_class import Holiday
from check_input import CheckInput
from candy import Candy
from random import randint


class CremeEggs(Candy):
    """
    Creme Eggs are Easter themed and are not lactose free and may contain traces of nuts.

    Pack Size - The creme eggs come in different packets, each containing a different number of creme eggs.
    """

    _generate_id = 0

    def __init__(self,
                 contains_nuts: bool,
                 pack_size: int,
                 name: str = "Creme Eggs",
                 description: str = "Creme Eggs are Easter themed and"
                                    " are not lactose free and may contain traces of nuts.",
                 product_id: str = ""
                 ) -> None:
        """
        Constructs a Creme Eggs.

        :param pack_size: containing a different number of creme eggs as an int
        :param contains_nuts: true if it contains nuts, false if not

        :precondition: pack_size must be a positive int
        """
        self._check_input(contains_nuts, pack_size, name, description, product_id)
        if len(product_id) == 0:
            product_id = "C%04dE" % CremeEggs._generate_id
        self._increment_id()
        self._contains_nuts = contains_nuts
        self._pack_size = pack_size
        self._name = name
        self._description = description
        self._product_id = product_id

    @staticmethod
    def generate_random_candy() -> Candy:
        """
        Generates a Creme eggs with random pack sizes.

        Pack Sizes is range from 1 to 5
        """
        contains_nuts = True if randint(0, 1) == 0 else False
        pack_size = randint(1, 5)
        return CremeEggs(contains_nuts, pack_size)

    @property
    def contains_nuts(self) -> bool:
        """
        Creme Eggs may contain traces of nuts.
        """
        return self._contains_nuts

    @property
    def lactose_free(self) -> bool:
        """
        Creme Eggs are not lactose free.
        """
        return False

    @property
    def pack_size(self) -> int:
        """
        Pack Size - The creme eggs come in different packets, each containing a different number of creme eggs.

        :return: pack size as an int
        """
        return self._pack_size

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
        Creme Eggs are Easter themed.
        """
        return Holiday.EASTER

    def _check_input(self,
                     contains_nut: bool,
                     pack_size: int,
                     name: str,
                     description: str,
                     product_id: str
                     ) -> None:
        CheckInput.check_type(pack_size, int)
        CheckInput.check_value_is_lower_equal_than_threshold(pack_size, 0)
        CheckInput.check_type(contains_nut, bool)
        CheckInput.check_all_input_type([name, description, product_id], str)