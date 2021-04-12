# Author:            Honghai Mei (Luke)
# Student Number:    A01075487
# Created time:      2021/4/10 12:19
# File Name:         factory.py
from typing import Type

from .ability import Ability
from .mode import Mode
from .move import Move
from .pokedex_object import PokedexObject
from .pokemon import Pokemon
from .request import Request
from .stat_class import Stat


class ModeFactory:
    """
    This class is mapping the request to the specific Mode Class.
    """

    @staticmethod
    def map_to_pokedex_object(request: Request) -> Type[PokedexObject]:
        """
        Return the pokedex class for a request.

        :param request a Request from command line
        :return a specific Mode class which matches request mode
        """
        if request.mode == Mode.POKEMON:
            return Pokemon
        elif request.mode == Mode.MOVE:
            return Move
        elif request.mode == Mode.ABILITY:
            return Ability
        else:
            return Stat
