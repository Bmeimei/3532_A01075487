# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/24 9:46 
# File Name:        dancing_skeleton.py
from enums_class import Fabric, Size, Stuffing, Holiday
from stuffed_animal import StuffedAnimal
from check_input import CheckInput
from dark import GrowsInDark


class DancingSkeleton(StuffedAnimal, GrowsInDark):
    """
    The dancing skeleton is made out of Acrylic yarn and stuffed with Polyester Fiberfill.
    This skeleton is sure to add to your Halloween decorations.
    The dancing skeleton also glows in the dark.
    """

    _generate_id = 0

    def __init__(self,
                 size: Size,
                 name: str = "Dancing Skeleton",
                 description: str = "Actually this skeleton is not terrible, it is cute as coco.",
                 product_id: str = ""
                 ) -> None:
        """
        Constructs a Dancing Skeleton.
        """
        self._check_input(size, name, description, product_id)
        if len(product_id) == 0:
            product_id = "S%04dD" % DancingSkeleton._generate_id
        self._increment_id()
        self._size = size
        self._name = name
        self._description = description
        self._product_id = product_id

    def _check_input(self,
                     size: Size,
                     name: str,
                     description: str,
                     product_id: str
                     ) -> None:
        CheckInput.check_type(size, Size)
        CheckInput.check_all_input_type([name, description, product_id], str)

    @staticmethod
    def holiday_type() -> Holiday:
        """
        Holiday Type is Halloween.
        :return:
        """
        return Holiday.HALLOWEEN

    @staticmethod
    def generate_random_animal() -> StuffedAnimal:
        size = Size.generate_random_child()
        return DancingSkeleton(size)

    @property
    def stuffing(self) -> Stuffing:
        """
        The dancing skeleton is made out of Polyester Fiberfill.
        """
        return Stuffing.POLYESTER_Fiberfill

    @property
    def size(self) -> Size:
        """
        Size of dancing skeleton.

        Size - This can either be Small, Medium or Large
        """
        return self._size

    @property
    def fabric(self) -> Fabric:
        """
        The dancing skeleton is made out of Acrylic yarn
        """
        return Fabric.ACRYLIC

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def product_id(self) -> str:
        return self._product_id

    @property
    def is_grow_in_dark(self) -> bool:
        """
        The dancing skeleton also glows in the dark.
        """
        return True