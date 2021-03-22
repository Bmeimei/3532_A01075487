# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/25 15:04 
# File Name:        journal.py

from library_item import LibraryItem


class Journal(LibraryItem):
    """
    Journals have names, issue number, and a publisher, and a DVD class
    """

    def __init__(self, call_num: str, title: str, num_copies: int, issue_number: str, publisher: str) -> None:
        """
        Constructs a journal.

        :param issue_number: Issue Number as a string.
        :param publisher: Publisher as a string.
        """
        super().__init__(call_num, title, num_copies)
        self._publisher = publisher
        self._issue_number = issue_number

    @property
    def publisher(self) -> str:
        """
        Gets the publisher.
        """
        return self._publisher

    @property
    def issue_number(self) -> str:
        """
        Gets the issue number.
        """
        return self._issue_number

    def __str__(self) -> str:
        """
        Journal String.
        """
        return f"---- Journal: {self.title} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number Of Copy: {self.num_copies}\n" \
               f"Issue Number: {self.issue_number}\n" \
               f"Publisher: {self.publisher}"
