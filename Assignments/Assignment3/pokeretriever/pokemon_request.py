# Author:            Honghai Mei (Luke)
# Student Number:    A01075487
# Created time:      2021/4/8 2:03
# File Name:         facade.py
from asyncio import get_event_loop

from .handler import Handler
from .pokedex_object import PokedexObject
from .pokemon_error import PokemonError
from .request import Request
from .factory import ModeFactory


class PokemonRequest:
    """
    Implement a facade class that will provide a simplified interface to the poke retriever package.
    Your program must control access to the package via the interface defined in this facade class
    """

    @staticmethod
    def execute_features(request: Request) -> list[PokedexObject]:
        """
        Execute Features. Return a bunch of Pokedex Object based on the sending request.
        """
        loop = get_event_loop()
        if request.input_data:
            response = loop.run_until_complete(Handler.process_single_request_task(request))
            return [ModeFactory.map_to_pokedex_object(request).map_to_object(response)]

        # Read File
        response = loop.run_until_complete(Handler.process_multiple_request_tasks(request))
        result = []
        for i in response:
            if "error" in i:
                pokemon_object = PokemonError("Error", -1)
            else:
                pokemon_object = ModeFactory.map_to_pokedex_object(request).map_to_object(i)
            result.append(pokemon_object)
        return result
