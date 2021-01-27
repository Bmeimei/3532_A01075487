""" This module houses the library"""
from book import Book
from dvd import DVD
from journal import Journal
from catalogue import Catalogue


class Library(Catalogue):
    """
    The Library consists of a list of books and provides an
    interface for users to check out, return and find books.
    """

    def __init__(self, item_list: list) -> None:
        """
        Initialize the library with a list of books.
        :param item_list: a sequence of book objects.
        """
        super().__init__(item_list)

    def check_out(self, call_number) -> None:
        """
        Check out an book with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        library_book = self._retrieve_item_by_call_number(call_number)
        if library_book.check_availability():
            status = self.reduce_item_count(call_number)
            if status:
                print("Checkout complete!")
            else:
                print(f"Could not find book with call number {call_number}"
                      f". Checkout failed.")
        else:
            print(f"No copies left for call number {call_number}"
                  f". Checkout failed.")

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

    def display_library_menu(self) -> None:
        """
        Display the library menu allowing the user to either access the
        list of books, check out, return, find, add, remove a book.
        """
        user_input = None
        while user_input != 7:
            print("\nWelcome to the Library!")
            print("-----------------------")
            print("1. Display all Item")
            print("2. Check Out an Item")
            print("3. Return an Item")
            print("4. Find an Item")
            print("5. Add an Item")
            print("6. Remove an Item")
            print("7. Quit")
            string_input = input("Please enter your choice (1-7)")

            # handle user pressing only enter in menu
            if string_input == '':
                continue

            user_input = int(string_input)

            if user_input == 1:
                self.display_available_items()
                user_input = input("Press Enter to continue")
            elif user_input == 2:
                call_number = input("Enter the call number of the book"
                                    " you wish to check out.")
                self.check_out(call_number)
            elif user_input == 3:
                call_number = input("Enter the call number of the book"
                                    " you wish to return.")
                self.return_item(call_number)
            elif user_input == 4:
                input_title = input("Enter the title of the book:")
                found_titles = set(self.find_items(input_title))
                print("We found the following:")
                if len(found_titles) > 0:
                    for title in found_titles:
                        print(title)
                else:
                    print("Sorry! We found nothing with that title")

            elif user_input == 5:
                self.add_item()

            elif user_input == 6:
                call_number = input("Enter the call number of the book")
                self.remove_item(call_number)

            elif user_input == 7:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 7.")

        print("Thank you for visiting the Library.")

    def display_available_items(self) -> None:
        """
        Display all the books in the library.
        """
        print("Books List")
        print("--------------", end="\n\n")
        for index, library_book in enumerate(self._item_list):
            print(index + 1, ": ", library_book)

    def reduce_item_count(self, call_number) -> bool:
        """
        Decrement the book count for an book with the given call number
        in the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the book was found and count decremented, false
        otherwise.
        """
        library_book = self._retrieve_item_by_call_number(call_number)
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
        library_book = self._retrieve_item_by_call_number(call_number)
        if library_book:
            library_book.increment_number_of_copies()
            return True
        return False


def generate_test_books() -> list:
    """
    Return a list of books with dummy data.
    :return: a list
    """
    book_list = [
        Book("100.200.300", "Harry Potter 1", 2, "J K Rowling"),
        Book("999.224.854", "Harry Potter 2", 5, "J K Rowling"),
        Book("631.495.302", "Harry Potter 3", 4, "J K Rowling"),
        Book("123.02.204", "The Cat in the Hat", 1, "Dr. Seuss"),
        Journal("100.132.126", "My Travel", 5, "123.1231.614a", "Luke"),
        DVD("123.456.123", "My Dream", 10, "Mike", "2020-03-10", "123")
    ]
    return book_list


def main() -> None:
    """
    Creates a library with dummy data and prompts the user for input.
    """
    book_list = generate_test_books()
    my_epic_library = Library(book_list)
    my_epic_library.display_library_menu()


if __name__ == '__main__':
    main()
