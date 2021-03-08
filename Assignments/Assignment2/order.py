# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/3/3 11:43 
# File Name:        order.py

from enums_class import InventoryEnum, Holiday
from check_input import CheckInput
from festive_season_factory import FestiveSeasonFactory, ChristmasFactory, HalloweenFactory, EasterFactory
import pandas as pd


class Order:
    """
    Each Order contains the following:

    • Order number
    • Product ID
    • Item - The type of item (Toy, StuffedAnimal and Candy).
    • Name of the item
    • A dictionary of product details.
        These details are the rest of the attributes of the item as specified in the excel sheet EXCEPT the name
        of the holiday — Easter, Christmas or Halloween.
    • The order should also contain a reference to the appropriate Factory object that can create this item.
    """

    def __init__(self, order_number: int, product_id: str, item_type: InventoryEnum, product_details: dict) -> None:
        """
        Constructs an order.
        """
        self._order_number = order_number
        self._product_id = product_id
        self._item_type = item_type
        self._product_details = product_details


class FactoryMapping:
    """
    FactoryMapping would map the holiday to the appropriate factory class.
    """

    @staticmethod
    def mapToFactory(holiday: Holiday) -> FestiveSeasonFactory:
        """
        Returns the factory class base on the specific holiday.
        """
        CheckInput.check_type(holiday, Holiday)
        if holiday == Holiday.CHRISTMAS:
            return ChristmasFactory()
        if holiday == Holiday.HALLOWEEN:
            return HalloweenFactory()
        if holiday == Holiday.EASTER:
            return EasterFactory()
        raise Exception("Invalid Festive!")


class OrderProcessing:
    """
    Your code must contain an OrderProcessor class that is responsible for reading each row of these files and creating
    and yielding an Order object. The OrderProcessor class contains a
    FactoryMapping which maps the holiday to the appropriate factory class.
    """

    def __init__(self, file_name: str):
        """
        Reads the excel file and generates a bunch of Orders
        :param file_name: file name must be a xlsx file.
        """
        self._file_name = file_name
        pd.read_excel(file_name)


def main():
    a = OrderProcessing("orders.xlsx")


if __name__ == '__main__':
    main()