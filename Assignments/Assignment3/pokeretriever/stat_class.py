# Author:            Honghai Mei (Luke)
# Student Number:    A01075487
# Created time:      2021/4/8 0:40
# File Name:         stat_class.py
from .pokedex_object import PokedexObject


class Stat(PokedexObject):
    """
    When in expanded mode, the user should be able to query for more details about each stat.
    Then in addition to the name and the base value, you would retrieve the following data:

    - Name
    - Id
    - Is Battery Only
    """

    def __init__(self, name: str, id_: int, is_battery_only: bool, move_damage_class: str) -> None:
        """
        Constructs a stat.
        :param name: name as a string
        :param id_: id as an int
        :param is_battery_only: is battery only as a boolean
        """
        super().__init__(name, id_)
        self._is_battery_only = is_battery_only
        self._move_damage_class = move_damage_class

    def __str__(self) -> str:
        """
        Formatted String of stat.
        """
        result = f"Name: {self._name}\n" \
                 f"ID: {self._id}\n" \
                 f"Is_Battery_Only: {self._is_battery_only}\n" \
                 f"Move Damage Class: {self._move_damage_class}"
        return result

    @staticmethod
    def map_to_object(information: dict) -> 'PokedexObject':
        name = information["name"]
        id_ = information["id"]
        is_battle_only = information["is_battle_only"]
        move_damage_class = information["move_damage_class"]["name"] if information["move_damage_class"] else "N/A"
        return Stat(name, id_, is_battle_only, move_damage_class)
