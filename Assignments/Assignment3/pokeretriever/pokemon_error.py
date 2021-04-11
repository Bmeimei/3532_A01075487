# Author:            Honghai Mei (Luke)
# Student Number:    A01075487
# Created time:      2021/4/9 0:36
# File Name:         pokemon_error.py
from .pokedex_object import PokedexObject


class PokemonError(PokedexObject):
    """
    This class occurs when error requests has some inaccurate data.
    """

    def __str__(self) -> str:
        return "An error occurred. Skipping this request."

    @staticmethod
    def map_to_object(information: dict) -> 'PokedexObject':
        pass
