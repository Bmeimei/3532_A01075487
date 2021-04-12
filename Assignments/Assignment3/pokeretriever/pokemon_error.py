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
        """
        When error orrcues, print this error message.
        """
        return "An error occurred. Skipping this request."

    @staticmethod
    def map_to_object(information: dict) -> 'PokedexObject':
        """
        This method is useless, we only need the __str__ method.
        """
        pass
