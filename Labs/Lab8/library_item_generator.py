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
    def create_book(item_info: dict) -> Book:
        """
        Creates a book.
        """
        author = input("Enter Author Name: ")
        item_info["author"] = author
        return Book(**item_info)

    @staticmethod
    def create_dvd(item_info: dict) -> DVD:
        """
        Creates a DVD.
        """
        release_day = input("Enter Release Date:")
        region_code = input("Enter Region Code:")
        item_info["release_date"] = release_day
        item_info["region_code"] = region_code
        return DVD(**item_info)

    @staticmethod
    def create_journal(item_info: dict) -> Journal:
        """
        Creates a Journal.
        """
        issue_number = input("Enter Issue Number: ")
        publisher = input("Enter Publisher Name: ")
        item_info["issue_number"] = issue_number
        item_info["publisher"] = publisher
        return Journal(**item_info)

    @staticmethod
    def create_library_item() -> LibraryItem:
        """
        Creates a library item.
        """
        while True:
            try:
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
                    call_number = input("Enter Call Number: ")
                    title = input("Enter title: ")
                    num_copies = int(input("Enter number of copies "
                                           "(positive number): "))
                    item_info = {"call_num": call_number,
                                 "title": title,
                                 "num_copies": num_copies}
                    return option_dict[option](item_info)

            except ValueError:
                print("-----------------\n"
                      "Invalid Input, Please tyr it again!\n"
                      "-----------------\n")
