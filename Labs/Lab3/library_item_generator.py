# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/25 15:09 
# File Name:        library_item_generator.py

from library_item import LibraryItem
from book import Book
from journal import Journal
from dvd import DVD


class LibraryItemGenerator:
    """
    Library Item Generator.
    """

    @staticmethod
    def create_book() -> Book:
        """
        Creates a book.
        """
        call_number = input("Enter Call Number: ")
        title = input("Enter title: ")
        num_copies = int(input("Enter number of copies "
                               "(positive number): "))
        author = input("Enter Author Name: ")
        return Book(call_number, title, num_copies, author)

    @staticmethod
    def create_dvd() -> DVD:
        """
        Creates a DVD.
        """
        call_number = input("Enter Call Number: ")
        title = input("Enter title: ")
        num_copies = int(input("Enter number of copies "
                               "(positive number): "))
        release_day = input("Enter Release Day:")
        region_code = input("Enter Region Code:")
        return DVD(call_number, title, num_copies, release_day, region_code)

    @staticmethod
    def create_journal() -> Journal:
        """
        Creates a Journal.
        """
        call_number = input("Enter Call Number: ")
        title = input("Enter Journal Name: ")
        num_copies = int(input("Enter Number of Copies: "))
        issue_number = input("Enter Issue Number: ")
        publisher = input("Enter Publisher Name: ")
        return Journal(call_number, title, num_copies, issue_number, publisher)

    @staticmethod
    def create_library_item() -> LibraryItem:
        """
        Creates a library item.
        """
        while True:
            option = input("1. Book\n"
                           "2. Journal\n"
                           "3. DVD\n"
                           "Please input the item option:")
            option_dict = {
                "1": LibraryItemGenerator.create_book,
                "2": LibraryItemGenerator.create_journal,
                "3": LibraryItemGenerator.create_dvd
            }
            if option not in option_dict:
                print("Invalid Command! Please type it again!")
            else:
                return option_dict[option]()