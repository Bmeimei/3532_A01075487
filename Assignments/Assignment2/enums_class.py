# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/24 0:28 
# File Name:        enums_class.py

from enum import Enum, auto
from random import sample

"""
This file contains all the enum class in this assignment.
"""


class Enums(Enum):
    """
    An interface enum class that would be implemented by all child enum class.
    """

    @classmethod
    def generate_random_child(cls) -> "Enums":
        """
        Generates a random child from the Enum list.
        """
        return sample(list(cls), 1)[0]

    def __str__(self) -> str:
        """
        Returns a string that represents the current enum value.
        """
        return self.name.title()

    @classmethod
    def map_str_to_enum(cls, word: str) -> "Enums":
        """
        Maps the string to the enum type.
        """
        for enum in list(cls):
            if word.strip() == str(enum).strip():
                return enum
        raise ValueError(f'{word} not exist in {str(cls)}')


class Holiday(Enums):
    """
    • Easter
    • Christmas
    • Halloween
    """
    EASTER = auto()
    CHRISTMAS = auto()
    HALLOWEEN = auto()


class InventoryEnum(Enums):
    """
    • Toys
    • Stuffed Animals
    • Candy
    """
    TOY = auto()
    STUFFED_ANIMAL = auto()
    CANDY = auto()

    def __str__(self) -> str:
        """
        Returns a string that represents the current enum value.
        """
        if self is InventoryEnum.STUFFED_ANIMAL:
            return "StuffedAnimal"
        return self.name.title()


class ToyEnum(Enums):
    """
    • Santa's Workshop
    • RC (Remote Controlled) Spider
    • Robot Bunny
    """
    SANTA_WORKSHOP = auto()
    REMOTE_CONTROLLER_SPIDER = auto()
    ROBOT_BUNNY = auto()

    def __str__(self) -> str:
        """
        Returns a string that represents the current enum value.
        """
        if self is ToyEnum.SANTA_WORKSHOP:
            return "Santa Workshop"
        if self is ToyEnum.REMOTE_CONTROLLER_SPIDER:
            return "Remote Controller Spider"
        return "Robot Bunny"


class StuffedAnimalEnum(Enums):
    """
    • Dancing Skeleton
    • Reindeer
    • Easter Bunny
    """
    DANCING_SKELETON = auto()
    REINDEER = auto()
    EASTER_BUNNY = auto()

    def __str__(self) -> str:
        """
        Returns a string that represents the current enum value.
        """
        if self is StuffedAnimalEnum.DANCING_SKELETON:
            return "Dancing Skeleton"
        if self is ToyEnum.REMOTE_CONTROLLER_SPIDER:
            return "Reindeer"
        return "Easter Bunny"


class CandyEnum(Enums):
    """
    • Pumpkin Caramel Toffee
    • Candy Canes
    • Creme Eggs
    """
    PUMPKIN_CARAMEL_TOFFEE = auto()
    CANDY_CANES = auto()
    CREME_EGGS = auto()

    def __str__(self) -> str:
        """
        Returns a string that represents the current enum value.
        """
        if self is CandyEnum.PUMPKIN_CARAMEL_TOFFEE:
            return "Pumpkin Caramel Toffee"
        if self is ToyEnum.REMOTE_CONTROLLER_SPIDER:
            return "Candy Canes"
        return "Creme Eggs"


class SpiderType(Enums):
    """
    The type of spider -
    This can either be a Tarantula or a Wolf Spider and nothing else.

    • Tarantula
    • Wolf Spider
    """
    TARANTULA = auto()
    WOLF_SPIDER = auto()

    def __str__(self) -> str:
        """
        Returns a string of name of this Spider Type.
        """
        if self is SpiderType.TARANTULA:
            return "Tarantula"
        return "Wolf Spider"


class Colours(Enums):
    """
    All Colours for the program needs.
    Including:

    - RobotBunnyColor
        • Orange
        • Blue
        • Pink

    - EasterBunnyColor
        • White
        • Grey
        • Pink
        • Blue

    - CandyCanesColor
        • Red
        • Green
    """
    ORANGE = auto()
    BLUE = auto()
    PINK = auto()
    WHITE = auto()
    GREY = auto()
    RED = auto()
    GREEN = auto()

    @staticmethod
    def get_random_robot_bunny_color() -> 'Colours':
        """
        Gets a random robot bunny color.
        """
        return sample([Colours.ORANGE, Colours.BLUE, Colours.PINK], 1)[0]

    @staticmethod
    def get_random_easter_bunny_color() -> 'Colours':
        """
        Gets a random robot bunny color.
        """
        return sample([Colours.WHITE, Colours.GREY, Colours.PINK, Colours.BLUE], 1)[0]

    @staticmethod
    def get_random_candy_canes_color() -> 'Colours':
        """
        Gets a random robot bunny color.
        """
        return sample([Colours.RED, Colours.GREEN], 1)[0]


class Stuffing(Enums):
    """
    This can either be Polyester Fiberfill or Wool

    • Polyester Fiberfill
    • Wool
    """
    POLYESTER_Fiberfill = auto()
    WOOL = auto()

    def __str__(self):
        """
        Returns the name of stuffing as a string.
        """
        if self is Stuffing.POLYESTER_Fiberfill:
            return "Polyester Fibrefill"
        return "Wool"


class Size(Enums):
    """
    Size - This can either be Small, Medium or Large

    • Small
    • Medium
    • Large
    """
    SMALL = auto()
    MEDIUM = auto()
    LARGE = auto()

    def __str__(self):
        """
        Returns the name of size as a string.
        """
        if self is Size.SMALL:
            return "S"
        if self is Size.MEDIUM:
            return "M"
        return "L"


class Fabric(Enums):
    """
    Fabric - This can either be Linen, Cotton or Acrylic

    • Linen
    • Cotton
    • Acrylic
    """
    LINEN = auto()
    COTTON = auto()
    ACRYLIC = auto()


class ToffeeVariety(Enums):
    """
    The Pumpkin Caramel Toffee is Halloween themed and is not lactose free and may contain traces of nuts.
    It comes in two varieties — Sea Salt and Regular.

    • Sea Salt
    • Regular
    """
    SEA_SALT = auto()
    REGULAR = auto()

    def __str__(self) -> str:
        """
        Returns a string of name of this Toffee Variety.
        """
        if self is ToffeeVariety.SEA_SALT:
            return "Sea Salt"
        return "Regular"
