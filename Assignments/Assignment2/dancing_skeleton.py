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
                 stuffing: Stuffing = Stuffing.POLYESTER_Fiberfill,
                 fabric: Fabric = Fabric.ACRYLIC,
                 has_grow: bool = True,
                 name: str = "Dancing Skeleton",
                 description: str = "Actually this skeleton is not terrible, it is cute as coco.",
                 product_id: str = ""
                 ) -> None:
        """
        Constructs a Dancing Skeleton.
        """
        self._check_input(size, stuffing, fabric, has_grow, name, description, product_id)
        if len(product_id) == 0:
            product_id = "S%04dD" % DancingSkeleton._generate_id
        self._increment_id()
        self._has_grow = has_grow
        super().__init__(name, description, product_id, size, stuffing, fabric)

    def _check_input(self,
                     size: Size,
                     stuffing: Stuffing,
                     fabric: Fabric,
                     has_grow: bool,
                     name: str,
                     description: str,
                     product_id: str
                     ) -> None:
        CheckInput.check_type(size, Size)
        CheckInput.check_type(stuffing, Stuffing)
        CheckInput.check_type(fabric, Fabric)
        CheckInput.check_type(has_grow)
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
    def has_grow(self) -> bool:
        """
        The dancing skeleton also glows in the dark.
        """
        return self._has_grow
