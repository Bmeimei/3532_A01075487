# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/3/3 11:43 
# File Name:        order.py
from factory_mapping import FactoryMapping
from enums_class import InventoryEnum, Holiday
from festive_season_factory import FestiveSeasonFactory
from math import isnan
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

    def __init__(self,
                 order_number: str,
                 product_id: str,
                 name: str,
                 quantity: int,
                 item_type: InventoryEnum,
                 product_details: dict,
                 factory: FestiveSeasonFactory) -> None:
        """
        Constructs an order.
        """
        self._order_number = order_number
        self._product_id = product_id
        self._name = name
        self._item_type = item_type
        self._quantity = quantity
        self._product_details = product_details
        self._factory = factory

    @property
    def order_number(self) -> str:
        """
        Getters for order number.
        """
        return self._order_number

    @property
    def product_id(self) -> str:
        """
        Getters for product id.
        """
        return self._product_id

    @property
    def name(self) -> str:
        """
        Getters for name.
        """
        return self._name

    @property
    def item_type(self) -> InventoryEnum:
        """
        Getters for item type.
        """
        return self._item_type

    @property
    def quantity(self) -> int:
        """
        Getters for quantity.
        """
        return self._quantity

    @property
    def product_details(self) -> dict:
        """
        Getters for product details.
        """
        return self._product_details

    @property
    def factory(self) -> FestiveSeasonFactory:
        """
        Getters for factory.
        """
        return self._factory

    def __str__(self) -> str:
        """
        Gets the string of the order information.
        """
        return f'Order {self._order_number},' \
               f' Item {str(self._item_type)},' \
               f' Product ID {self._product_id},' \
               f' Name "{self._name}",' \
               f' Quantity {self._quantity} '


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
        self._excel_rows_info = OrderProcessing.get_rows_info(pd.read_excel(file_name).T.to_dict())

    def __iter__(self) -> Order:
        """
        Iterator of the Order Processing.
        Every time call this iterator would generate an order until the orders have been processed all.
        """
        yield from (self.map_to_order_from_row(row) for row in self._excel_rows_info)

    def process_orders(self) -> iter:
        """
        Returns the generator of the processing orders.
        """
        return iter(self)

    @staticmethod
    def get_rows_info(excel_dict: dict) -> list:
        """
        Generates the rows list from an excel dict by pandas.
        """
        result = []
        for key, value in excel_dict.items():
            result.append({k: v for k, v in value.items() if isinstance(v, str) or not isnan(v)})
        return result

    @staticmethod
    def map_to_order_from_row(row: dict) -> Order:
        holiday = Holiday.map_str_to_enum(row.pop('holiday', None))
        order_number = row.pop('order_number', None)
        product_id = row.pop('product_id', None)
        name = row.pop('name', None)
        quantity = int(row.pop('quantity', None))
        item_type = InventoryEnum.map_str_to_enum(row.pop('item', None))
        factory = FactoryMapping.map_to_factory(holiday)
        row = FactoryMapping.map_attributes(row)
        return Order(order_number, product_id, name, quantity, item_type, row, factory)
