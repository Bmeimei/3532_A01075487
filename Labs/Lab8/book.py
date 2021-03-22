# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/25 16:14 
# File Name:        book.py

from library_item import LibraryItem


class Book(LibraryItem):
    """
    Book.
    """

    def __init__(self, call_num: str, title: str, num_copies: int, author: str) -> None:
        super().__init__(call_num, title, num_copies)
        self._author = author

    @property
    def author(self) -> str:
        """
        Gets author.
        """
        return self._author

    def __str__(self) -> str:
        """
        Book String.
        """
        return f"---- Book: {self.title} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self.num_copies}\n" \
               f"Author: {self.author}"
