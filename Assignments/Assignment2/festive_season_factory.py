# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/23 20:54 
# File Name:        festive_season_factory.py
from abc import ABC, abstractmethod

from toy import Toy
from stuffed_animal import StuffedAnimal
from candy import Candy


class FestiveSeasonFactory(ABC):

    @abstractmethod
    @property
    def toys(self) -> Toy:
        """
        Toys.

        For each festive season, the store stocks a unique toy.
        Despite that, there are some properties of each toy that all toys have in common.
        These are:

        • Whether the toy is battery operated or not.
        • The minimum recommended age of the child that the toy is safe for.
        • A name
        • A description
        • Product ID (A unique combination of letters and numbers)

        :return: Toys
        """
        pass

    @abstractmethod
    @property
    def stuffed_animals(self) -> StuffedAnimal:
        """
        Stuffed animals.

        All stuffed animals have the following attributes:

        • Stuffing - This can either be Polyester Fiberfill or Wool
        • Size - This can either be Small, Medium or Large
        • Fabric - This can either be Linen, Cotton or Acrylic
        • Name
        • Description
        • Product ID

        :return: Stuffed Animals
        """
        pass

    @abstractmethod
    @property
    def candy(self) -> Candy:
        """
        Candy.

        All candies have the following properties:

        • A flag to check if it contains any nuts
        • A flag to check if it is lactose free.
        • Name • Description
        • Product ID

        :return: Candy
        """
        pass