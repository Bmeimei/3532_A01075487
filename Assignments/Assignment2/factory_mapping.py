from festive_season_factory import FestiveSeasonFactory, ChristmasFactory, HalloweenFactory, EasterFactory
from enums_class import Holiday, SpiderType, Colours, ToffeeVariety, Stuffing, Size, Fabric


class FactoryMapping:
    """
    FactoryMapping would map the holiday to the appropriate factory class.
    """

    @staticmethod
    def map_to_factory(holiday: Holiday) -> FestiveSeasonFactory:
        """
        Returns the factory class base on the specific holiday.
        """
        factory = None
        if holiday == Holiday.CHRISTMAS:
            factory = ChristmasFactory
        if holiday == Holiday.HALLOWEEN:
            factory = HalloweenFactory
        if holiday == Holiday.EASTER:
            factory = EasterFactory
        if factory is None or factory.get_instance() is None:
            raise TypeError("Invalid Holiday Type!")
        return factory.get_instance()

    @staticmethod
    def map_attributes(order: dict) -> dict:
        """
        Maps all the attributes into specific enums type or boolean or number, and return the dict after mapping.
        """
        map_dict = {
            "has_batteries": FactoryMapping.cast_str_to_bool,
            "has_glow": FactoryMapping.cast_str_to_bool,
            "has_lactose": FactoryMapping.cast_str_to_bool,
            "has_nuts": FactoryMapping.cast_str_to_bool,
            "min_age": int,
            "num_rooms": int,
            "num_sound": int,
            "pack_size": int,
            "dimensions": lambda x: float(x.replace(",", '.')),
            "spider_type": SpiderType.map_str_to_enum,
            "colour": Colours.map_str_to_enum,
            "variety": ToffeeVariety.map_str_to_enum,
            "stuffing": Stuffing.map_str_to_enum,
            "size": Size.map_str_to_enum,
            "fabric": Fabric.map_str_to_enum
        }
        for key, value in map_dict.items():
            if key in order:
                order[key] = value(order[key])
        return order

    @staticmethod
    def cast_str_to_bool(word: str) -> bool:
        """
        Casts string to boolean.
        :param word:
        :return:
        """
        word = word.upper()
        if word == "N":
            return False
        elif word == "Y":
            return True
        raise ValueError("%s is not a valid string to boolean!" % str)