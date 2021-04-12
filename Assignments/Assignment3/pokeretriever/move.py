# Author:            Honghai Mei (Luke)
# Student Number:    A01075487
# Created time:      2021/4/7 23:09
# File Name:         move.py
from .pokedex_object import PokedexObject


class Move(PokedexObject):
    """
    The user should be able to provide the name or id of an Ability and query its information.
    You want to create an Move Class that can store (and ultimately be used to report) the following data:

    - Name
    - ID
    - Generation
    - Accuracy
    - PP
    - Power
    - Type
    - Damage Class
    - Effect(Short)
    """

    def __init__(self, name: str, id_: int, generation: str, accuracy: int,
                 pp: int, power: int, type_: str, damage_class: str, effect: str) -> None:
        """
        Constructs a Move object.
        """
        super().__init__(name, id_)
        self._generation = generation
        self._accuracy = accuracy
        self._pp = pp
        self._power = power
        self._type = type_
        self._damage_class = damage_class
        self._effect = effect

    def __str__(self) -> str:
        """
        Formats Move.
        :return: a formatted string that represents Move
        """
        return f"Name: {self.name}\n" \
               f"ID: {self.id}\n" \
               f"Generation: {self._generation}\n" \
               f"Accuracy: {self._accuracy}\n" \
               f"PP: {self._pp}\n" \
               f"Power: {self._power}\n" \
               f"Type: {self._type}\n" \
               f"Damage Class: {self._damage_class}\n" \
               f"Effect (Short): {self._effect}"

    @staticmethod
    def map_to_object(information: dict) -> 'PokedexObject':
        """
        Maps the information dict to Move.
        :param information: the response dict
        :return: an Move instance
        """
        name = information["name"]
        id_ = information["id"]
        generation = information["generation"]["name"]
        accuracy = information["accuracy"]
        pp = information["pp"]
        power = information["power"]
        type_ = information["type"]["name"]
        damage_class = information["damage_class"]["name"]
        effect = information["effect_entries"][0]["short_effect"]
        return Move(name, id_, generation, accuracy, pp, power, type_, damage_class, effect)
