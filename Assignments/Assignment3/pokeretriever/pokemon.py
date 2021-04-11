# Author:            Honghai Mei (Luke)
# Student Number:    A01075487
# Created time:      2021/4/7 22:57
# File Name:         pokemon.py
from asyncio import get_event_loop

from .handler import Handler
from .pokedex_object import PokedexObject
from .stat_class import Stat
from .ability import Ability
from .move import Move


class Pokemon(PokedexObject):
    """
    The user should be able to provide the name or id of a Pokémon and query its information.
    You want to create a Pokemon Class that can store (and ultimately be used to report) the following data:

    - Name
    - ID
    - Height
    - Weight
    - Stats
    - Types
    - Abilities
    - Moves
    """

    def __init__(self, name: str, id_: int, height: int, weight: int, stats: list[dict], types: list[dict],
                 abilities: list[dict], moves: list[dict], is_expanded: bool) -> None:
        """
        Constructs a Pokemon Object.
        """
        super().__init__(name, id_)
        self._height = height
        self._weight = weight
        self._stats = stats
        self._types = types
        self._abilities = abilities
        self._moves = moves
        self._is_expanded = is_expanded
        self._check_if_expanded()

    def _check_if_expanded(self) -> None:
        """
        Checks if this Pokemon needs expanded information.
        If expanded, it would convert the stats, abilities and moves to the Stats, Ability and Move Object.
        """
        if self._is_expanded:
            self._map_stats_to_stats_list()
            self._map_abilities_to_ability_list()
            self._map_moves_to_move_list()

    def _map_stats_to_stats_list(self) -> None:
        """
        Maps the stats to stats objects list.
        """
        url_list = [stat["stat"]["url"] for stat in self._stats]
        loop = get_event_loop()
        result = loop.run_until_complete(Handler.process_request_tasks_with_default_urls(url_list))
        self._stats = [Stat.map_to_object(i) for i in result]

    def _map_abilities_to_ability_list(self) -> None:
        """
        Maps the abilities to Ability object list.
        """
        url_list = [ability["ability"]["url"] for ability in self._abilities]
        loop = get_event_loop()
        result = loop.run_until_complete(Handler.process_request_tasks_with_default_urls(url_list))
        self._abilities = [Ability.map_to_object(i) for i in result]

    def _map_moves_to_move_list(self) -> None:
        """
        Maps the moves to move object list.
        """
        url_list = [move["move"]["url"] for move in self._moves]
        loop = get_event_loop()
        result = loop.run_until_complete(Handler.process_request_tasks_with_default_urls(url_list))
        self._moves = [Move.map_to_object(i) for i in result]

    def _map_stats_to_tuples_str(self) -> str:
        """
        Converts stats to strings.
        """
        return "".join(map(lambda x: str(x) + "\n", [(element["stat"]["name"],
                                                      element["base_stat"]) for element in self._stats]))

    def _map_abilities_to_str(self) -> str:
        """
        Converts abilities to strings.
        """
        result = ""
        for ability in self._abilities:
            result += ability["ability"]["name"] + "\n\n"
        return result

    def _map_moves_to_tuples_str(self) -> str:
        """
        Converts moves to strings.
        """
        result = ""
        for move in self._moves:
            name = move["move"]["name"]
            level = move["version_group_details"][0]["level_learned_at"]
            move_tuple = (f"Move Name: {name}", f"Level acquired: {level}")
            result += str(move_tuple) + "\n\n"

        return result

    def _expanded_str(self) -> str:
        """
        Formatted String with expanded information.
        """
        new_line = "\n"
        result = f"Name: {self.name}\n" \
                 f"ID: {self.id}\n" \
                 f"Height: {self._height}\n" \
                 f"Weight: {self._weight}\n" \
                 f"Types: {self._types[0]['type']['name']}\n\n" \
                 f"Stats:\n" \
                 f"------\n\n" \
                 f"{''.join(map(lambda x: (str(x) + new_line + new_line), self._stats))}\n" \
                 f"Abilities:\n" \
                 f"------\n\n" \
                 f"{''.join(map(lambda x: (str(x) + new_line + new_line), self._abilities))}\n" \
                 f"Moves:\n" \
                 f"------\n\n" \
                 f"{''.join(map(lambda x: (str(x) + new_line + new_line), self._moves))}\n"
        return result

    def __str__(self) -> str:
        """
        Formatted the pokemon.
        """
        if self._is_expanded:
            return self._expanded_str()
        result = f"Name: {self.name}\n" \
                 f"ID: {self.id}\n" \
                 f"Height: {self._height}\n" \
                 f"Weight: {self._weight}\n" \
                 f"Types: {self._types[0]['type']['name']}\n\n" \
                 f"Stats:\n" \
                 f"------\n" \
                 f"{self._map_stats_to_tuples_str()}\n" \
                 f"Abilities:\n" \
                 f"------\n" \
                 f"{self._map_abilities_to_str()}\n" \
                 f"Moves:\n" \
                 f"------\n" \
                 f"{self._map_moves_to_tuples_str()}"
        return result

    @staticmethod
    def map_to_object(information: dict) -> 'PokedexObject':
        name = information["name"]
        id_ = information["id"]
        height = information["height"]
        weight = information["weight"]
        stats = information["stats"]
        types = information["types"]
        abilities = information["abilities"]
        moves = information["moves"]
        is_expanded = information["is_expanded"]
        return Pokemon(name, id_, height, weight, stats, types, abilities, moves, is_expanded)
