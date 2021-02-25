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

    def __init__(self, size: Size) -> None:
        """
        Constructs a Dancing Skeleton.
        """
        self._check_input(size)
        self._increment_id()
        self._size = size

    def _check_input(self, size: Size) -> None:
        CheckInput.check_type(size, Size)

    @property
    def holiday_type(self) -> Holiday:
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
        return "Dancing Skeleton"

    @property
    def description(self) -> str:
        return "Actually this skeleton is not terrible, it is cute as coco."

    @property
    def product_id(self) -> str:
        return "S%04dD" % self._generate_id

    @property
    def is_grow_in_dark(self) -> bool:
        """
        The dancing skeleton also glows in the dark.
        """
        return True