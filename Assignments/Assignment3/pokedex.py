# Author:            Honghai Mei (Luke)
# Student Number:    A01075487
# Created time:      2021/3/31 11:11
# File Name:         pokedex.py

import asyncio
import aiohttp
import argparse
from enum import Enum


class Mode(Enum):
    POKEMON = "Pokemon"
    ABILITY = "Ability"
    MOVE = "Move"


class Pokedex:

    def __init__(self) -> None:
        pass

    @staticmethod
    def setup_command_line() -> 'Pokedex':
        """
        Gets command line arguments by argparse.
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("mode", help="The mode to the Pokemon. "
                                         "Pokemon mode, the input will be an id or the name of a pokemon. "
                                         "The pokedex will query pokemon information.\n"
                                         "Ability mode, "
                                         "the input will be an id or the name of a ability. "
                                         "These are certain effects that pokemon can enable. "
                                         "The pokedex will query the ability information.\n"
                                         "Move mode, the input will be an id or the name of a pokemon move. "
                                         "These are the attacks and actions pokemon can take. "
                                         "The pokedex will query the move information.")

        group = parser.add_mutually_exclusive_group()
        group.add_argument("-f", "--inputfile", help="The text file that has the id of digit and the name of string."
                                                     "The file name must end with a .txt extension")
        group.add_argument("-d", "--inputdata", help="The input data that has the id "
                                                     "of digit and the name of string.")

        parser.add_argument("-e", "--expended", help="Optional flag, Get extra information if it is provided.",
                            action="store_true")
        parser.add_argument("o", "--output", help="Print the output in default. If provided,"
                                                  " a filename (with a .txt extension) must also be provided."
                                                  " and the query result should be printed to the specified text file.")
