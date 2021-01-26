# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/25 15:04 
# File Name:        journal.py

from library_item import LibraryItem


class Journal(LibraryItem):
    """
    Journals have names, issue number, and a publisher, and a DVD class
    """

    def __init__(self, call_num: str, names: str, issue_number: int, publisher: str) -> None:
        super().__init__(call_num, names, issue_number, publisher)

    def __str__(self) -> str:
        return f"---- Journal: {self.get_title()} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Issue Number: {self._num_copies}\n" \
               f"Publisher: {self._author}"