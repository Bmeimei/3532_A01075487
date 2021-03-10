# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/23 20:47 
# File Name:        inventory.py

from item import Item
from check_input import CheckInput
from santa_work_shop import SantaWorkShop
from creme_eggs import CremeEggs


class Inventory:
    """
    The Inventory that contains a bunch of items.

    This class is using Singleton design pattern to promise only 1 inventory exists in this thread.
    """

    __instance = None

    def __init__(self) -> None:
        """
        Constructs an Inventory by using Singleton.
        All the item is out of stock at the beginning.
        """
        if Inventory.__instance is not None:
            raise Exception("The store already has one inventory! Please don't create a new one!")
        Inventory.__instance = self
        self._items = dict()

    @staticmethod
    def get_inventory() -> 'Inventory':
        """
        Gets the instance of this inventory. Actually it is returning the same instance in this thread.
        """
        if Inventory.__instance is None:
            Inventory()
        return Inventory.__instance

    def import_items(self, item: Item, count: int = 1) -> None:
        """
        Add Items stock. If the item already existed in the inventory, increase the count.
        Else put the item into inventory.

        :param item: Item
        :param count: the number of item, default is 1
        """
        CheckInput.check_type(item, Item)
        CheckInput.check_type(count, int)
        CheckInput.check_value_is_lower_equal_than_threshold(count, 0)
        if item in self._items.keys():
            self._items[item] += count
            return None
        self._items[item] = count

    def check_if_item_enough(self, item: Item, count: int) -> bool:
        """
        Checks if the inventory has enough stock for exporting this item.

        :return: True if it has enough items, False if not
        """
        CheckInput.check_type(item, Item)
        CheckInput.check_type(count, int)
        CheckInput.check_value_is_lower_equal_than_threshold(count, 0)
        if item not in self._items.keys():
            raise False
        return self._items[item] >= count

    def export_items(self, item: Item, count: int = 1) -> None:
        """
        Exports Items from the inventory.

        :param item: Item
        :param count: the number of item, default is 1
        """
        CheckInput.check_type(item, Item)
        CheckInput.check_type(count, int)
        CheckInput.check_value_is_lower_equal_than_threshold(count, 0)
        if item not in self._items.keys():
            raise KeyError(item, "Inventory doesn't have this item")
        if self._items[item] < count:
            raise ValueError("The Inventory doesn't have enough stock for %s" % item)
        self._items[item] -= count

    def check_stock(self) -> None:
        """
        This allows the cashier to check what is currently in stock and will also provide a status indicator for
        items if the stock for this item is LOW, VERY LOW, IN STOCK, or OUT OF STOCK.
        """
        if not self._items:
            print("Currently No Items In Store!")
            return None
        for item, count in self._items.items():
            if count >= 10:
                status = "IN STOCK"
            elif 3 <= count < 10:
                status = "LOW"
            elif 0 < count < 3:
                status = "VERY LOW"
            else:
                status = "OUT OF STOCK"

            print("%s - %s" % (item, status))

    def __iter__(self) -> iter:
        """
        Generates an iterator for the inventory.
        """
        return iter(self._items)


def main():
    a = Inventory.get_inventory()
    item = SantaWorkShop(3.4, 2)
    a.import_items(item, 10)
    a.import_items(SantaWorkShop(3.4, 2))
    a.import_items(SantaWorkShop(3.4, 2))
    a.import_items(CremeEggs(False, 30), 5)
    a.check_stock()


if __name__ == '__main__':
    main()
