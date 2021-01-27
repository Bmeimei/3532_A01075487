from abc import ABC, abstractmethod


class LibraryItem(ABC):
    """
    Represents a single book in a library which is identified through
    it's call number.
    """

    def __init__(self, call_num: str, title: str, num_copies: int, author: str):
        """
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :param author: a string
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        self._call_num = call_num
        self._title = title
        self._num_copies = num_copies
        self._author = author

    def get_title(self) -> str:
        """
        Returns the title of the item
        :return: a string
        """
        return self._title.title()

    def increment_number_of_copies(self) -> None:
        """
        Set's the number of copies of an item
        """
        self._num_copies += 1

    def decrement_number_of_copies(self) -> None:
        """
        Set's the number of copies of an item
        """
        if self._num_copies == 0:
            print("Are you sure? This item has no copy now!")
            return None
        self._num_copies -= 1

    def get_num_copies(self) -> int:
        """
        Returns the number of copies that are available for this
        specific item.
        :return: an int
        """
        return self._num_copies

    @property
    def call_number(self) -> str:
        """
        Right, this here is another way of using properties.
        We use decorators. The @property decorator defines a property
        that only allows us to GET a value and not set one.

        I want to point out that I have not expected you to do this in
        your labs. I'm using this as an opportunity to introduce you to
        a new way of avoiding mechanical getters and setters.
        :return:
        """
        return self._call_num

    # @call_number.setter
    # def call_number(self, value):
    #     """
    #     This is the decorator way to create a SET property. This would
    #     allow us to invoke this method by simply saying
    #     my_book.call_number = "102.345.992". I've commented this out
    #     since call numbers should not need a setter.
    #     :param value: a string
    #     :precondition value: a unique call number identifier
    #     """
    #     self._call_num = value

    def check_availability(self) -> bool:
        """
        Returns True if the book is available and False otherwise
        :return: A Boolean
        """
        return self._num_copies >= 1

    @abstractmethod
    def __str__(self) -> str:
        pass