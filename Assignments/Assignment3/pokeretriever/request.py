# Author:            Honghai Mei (Luke)
# Student Number:    A01075487
# Created time:      2021/4/8 1:49
# File Name:         request.py
import argparse

from Assignments.Assignment3.pokeretriever.mode import Mode


class Request:
    """
    Request is a class that contains all the data gathered by the argparse module.
    """

    def __init__(self) -> None:
        """
        Constructs an empty Request.
        """
        self.mode = None
        self.input_file = None
        self.input_data = None
        self.expanded = None
        self.output = None

    def __str__(self) -> str:
        """
        Formats a Request.
        """
        return "Request: {Mode: %s, Input File: %s, Input Data: %s, is_expanded: %s, Output: %s}" % \
               (self.mode, self.input_file, self.input_data, self.expanded, self.output)

    @staticmethod
    def setup_command_line() -> 'Request':
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

        parser.add_argument("-e", "--expanded", help="Optional flag, Get extra information if it is provided.",
                            action="store_true")
        parser.add_argument("-o", "--output", default="print", help="Print the output in default. If provided, "
                                                                    "a filename (with a .txt extension) must also be "
                                                                    "provided. "
                                                                    "and the query result should be printed to the "
                                                                    "specified text file.")

        try:
            request = Request()
            args = parser.parse_args()
            mode = Mode(args.mode.title())
            file = args.inputfile
            data = args.inputdata
            expanded = args.expanded
            output = args.output

            request.mode = mode
            request.input_file = file
            request.input_data = data
            request.expanded = expanded
            request.output = output

            return request

        except Exception as e:
            print(f"Error! Could not read arguments.\n{e}")
            quit()
