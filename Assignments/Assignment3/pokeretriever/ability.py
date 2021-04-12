# Author:            Honghai Mei (Luke)
# Student Number:    A01075487
# Created time:      2021/4/7 23:07
# File Name:         ability.py
from .pokedex_object import PokedexObject


class Ability(PokedexObject):
    """
    The user should be able to provide the name or id of an Ability and query its information.
    You want to create an Ability Class that can store (and ultimately be used to report) the following data:

    - Name
    - ID
    - Generation
    - Effect
    - Effect(Short) (short_effect)
    - Pokemon
    """

    def __init__(self, name: str, id_: int,
                 generation: str, effect: str, short_effect: str, pokemon: list[str]) -> None:
        """
        Constructs an Ability Object.
        """
        super().__init__(name, id_)
        self._generation = generation
        self._effect = effect
        self._short_effect = short_effect
        self._pokemon = pokemon

    def __str__(self) -> str:
        """
        Formats Ability.
        :return: a string that represents Ability
        """
        return f"Name: {self.name}\n" \
               f"ID: {self.id}\n" \
               f"Generation: {self._generation}\n" \
               f"Effect: {self._effect}\n" \
               f"Effect (Short): {self._short_effect}\n" \
               f"Pokemon: {self._get_pokemon_names()}"

    def _get_pokemon_names(self) -> str:
        """
        Gets the names from pokemon list.
        """
        result = ""
        for name in self._pokemon:
            result += name + ", "
        return result[:-2]

    @staticmethod
    def map_to_object(information: dict) -> 'PokedexObject':
        """
        Maps the information dict to Ability.
        :param information: the response dict
        :return: an Ability instance
        """
        name = information["name"]
        id_ = information["id"]
        generation = information["generation"]["name"]
        effect = information["effect_entries"][1]["effect"]
        short_effect = information["effect_entries"][1]["short_effect"]
        pokemon = [name["pokemon"]["name"] for name in information["pokemon"]]
        return Ability(name, id_, generation, effect, short_effect, pokemon)
