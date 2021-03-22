# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/25 11:08 
# File Name:        catalogue.py

from library_item import LibraryItem
import difflib
from library_item_generator import LibraryItemGenerator


class Catalogue:
    """
    Implement a Catalogue class will now be responsible for maintaining a list of books.
    Move all the methods and code related to searching, adding and removing books to this new class
    """

    def __init__(self, item_list: list[LibraryItem]) -> None:
        """
        Initialize the library with a list of books.
        :param item_list: a sequence of book objects.
        """
        self._item_list = item_list

    @property
    def item_list(self) -> list[LibraryItem]:
        """
        Property for item list.

        :return: the property for item list
        """
        return self._item_list

    def find_items(self, title: str) -> list:
        """
        Find books with the same and similar title.
        :param title: a string
        :return: a list of titles.
        """
        title_list = [library_book.get_title() for library_book in self._item_list]
        results = difflib.get_close_matches(title.title(), title_list, cutoff=0.2)
        return results

    def add_item(self) -> None:
        """
        Add a brand new book to the library with a unique call number.
        """
        new_item = LibraryItemGenerator.create_library_item()

        found_item = self.retrieve_item_by_call_number(new_item.call_number)
        if found_item:
            print(f"Could not add Item with call number "
                  f"{new_item.call_number}. It already exists. ")
        else:
            self._item_list.append(new_item)
            print("Item added successfully! Item details:")
            print(new_item)

    def remove_item(self, call_number: str) -> None:
        """
        Remove an existing book from the library
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        found_book = self.retrieve_item_by_call_number(call_number)
        if found_book:
            self._item_list.remove(found_book)
            print(f"Successfully removed {found_book.get_title()} with "
                  f"call number: {call_number}")
        else:
            print(f"book with call number: {call_number} not found.")

    def reduce_item_count(self, call_number) -> bool:
        """
        Decrement the book count for an book with the given call number
        in the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the book was found and count decremented, false
        otherwise.
        """
        library_book = self.retrieve_item_by_call_number(call_number)
        if library_book:
            library_book.decrement_number_of_copies()
            return True
        return False

    def increment_item_count(self, call_number) -> bool:
        """
        Increment the book count for an book with the given call number
        in the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the book was found and count incremented, false
        otherwise.
        """
        library_book = self.retrieve_item_by_call_number(call_number)
        if library_book:
            library_book.increment_number_of_copies()
            return True
        return False

    def return_item(self, call_number) -> None:
        """
        Return an book with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        status = self.increment_item_count(call_number)
        if status:
            print("book returned successfully!")
        else:
            print(f"Could not find book with call number {call_number}"
                  f". Return failed.")

    def retrieve_item_by_call_number(self, call_number: str) -> LibraryItem or None:
        """
        A private method that encapsulates the retrieval of an book with
        the given call number from the library.
        :param call_number: a string
        :return: book object if found, None otherwise
        """
        for library_item in self._item_list:
            if library_item.call_number == call_number:
                return library_item
        return None
