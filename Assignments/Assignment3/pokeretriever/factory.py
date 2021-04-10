# Author:            Honghai Mei (Luke)
# Student Number:    A01075487
# Created time:      2021/4/10 12:19
# File Name:         factory.py
from typing import Type

from Assignments.Assignment3.pokeretriever.ability import Ability
from Assignments.Assignment3.pokeretriever.mode import Mode
from Assignments.Assignment3.pokeretriever.move import Move
from Assignments.Assignment3.pokeretriever.pokedex_object import PokedexObject
from Assignments.Assignment3.pokeretriever.pokemon import Pokemon
from Assignments.Assignment3.pokeretriever.request import Request
from Assignments.Assignment3.pokeretriever.stat_class import Stat


class ModeFactory:
    """
    This class is mapping the request to the specific Mode Class.
    """

    @staticmethod
    def map_to_pokedex_object(request: Request) -> Type[PokedexObject]:
        """
        Return the pokedex class for a request.
        """
        if request.mode == Mode.POKEMON:
            return Pokemon
        elif request.mode == Mode.MOVE:
            return Move
        elif request.mode == Mode.ABILITY:
            return Ability
        else:
            return Stat
