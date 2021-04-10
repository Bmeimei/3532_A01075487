# Author:            Honghai Mei (Luke)
# Student Number:    A01075487
# Created time:      2021/4/7 23:00
# File Name:         pokedex_object.py

from abc import ABC, abstractmethod


class PokedexObject(ABC):
    """
    PokedexObject is a base class that defines the name and id parameter.
    The Pokemon , Moves , Stat , and Ability classes should inherit from this class.
    """

    def __init__(self, name: str, id_: int) -> None:
        """
        Constructs a Pokedex Object.

        :param name: name of the pokedex object as a string
        :param id_: id of the pokedex object as an int
        """
        self._name = name
        self._id = id_

    @property
    def name(self) -> str:
        """
        Getter for name.
        """
        return self._name

    @property
    def id(self) -> int:
        """
        Getter for id.
        """
        return self._id

    @abstractmethod
    def __str__(self) -> str:
        """
        Pokedex object should have a toString method.
        """
        pass

    @staticmethod
    @abstractmethod
    def map_to_object(information: dict) -> 'PokedexObject':
        """
        Maps a dict to this pokedex Object.
        """
        pass
