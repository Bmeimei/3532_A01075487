# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/8 10:36 
# File Name:        dictionary.py

from file_handler import FileHandler, InvalidFileTypeError
from difflib import get_close_matches
from file_extensions import FileExtensions


class Dictionary:
    """
    This module is responsible for housing the dictionary class (alongside any custom exceptions that apply to
    the dictionary) and any driver methods that run the program.

    - A dictionary needs to be loaded.
      Implement a load_dictionary(self, filepath) method that is responsible for loading data into a dictionary
    - A dictionary needs to be able to look up the definition of a word.
      Implement a query_definition(self, word) method that returns the definition(s) of a given word.
    - A way to keep track of whether the dictionary has been loaded or not.
      This will be useful when testing your applications.

    """

    def __init__(self) -> None:
        """
        Initializes the default dictionary which is None.
        """
        self.dictionary = None

    def load_dictionary(self, filepath: str = "data.json",
                        file_extensions: FileExtensions = FileExtensions.JSON) -> None:
        """
        Loading data into a dictionary.
        Default file path is 'data'.json', and default File extensions is JSON

        :param file_extensions: The file extensions as a FileExtensions
        :param filepath: The file path as a string.
        """
        if filepath.strip() == "":
            filepath = "data.json"
        self.dictionary = FileHandler.load_data(filepath, file_extensions)

    def query_definition(self, word: str) -> list:
        """
        Returns the definition(s) of a given word from the dictionary.

        :param word: a word as a string
        :return: the definition(s) of a given word as a string
        :raise UnInitializationError: if user calls this function without initialize the dictionary
        :raise TypeError: if word is not a string
        :raise NoSuchWordError: if user types a really nonsense word that match function can't find it
        :raise KeyError: if the query word not exist in the dictionary
        """
        if not isinstance(word, str):
            raise TypeError()
        if self.dictionary is None:
            raise UnInitializationError()

        word_list = [key for key in map(lambda x: x.lower(), self.dictionary.keys())]
        similar_word = get_close_matches(word.lower(), word_list)
        if not similar_word:
            raise NoSuchWordError(word)
        result = self.dictionary[similar_word[0]]
        return result

    @staticmethod
    def save_queries(queries: dict, file_name: str = "saved_queries.txt") -> None:
        """
        Save the definitions and words that the user queries to a text file.

        :param queries: the user queries as a dict, keys are words, values are definitions
        :param file_name: the output file txt, default is saved_queries.txt
        """
        FileHandler.write_lines(file_name, queries)

    @staticmethod
    def querying_words_from_dictionary(output_file: str = "saved_queries.txt") -> None:
        """
        Execute the querying dictionary program for user.
        """
        try:
            file_name = input("Please type the dictionary file you want to load(Optional, Default file is"
                              " 'data.json'):")
            extension = FileHandler.choose_extension_of_string(file_name)
            dictionary = Dictionary()
            dictionary.load_dictionary(file_name, extension)
            queries = dict()
            print("Welcome To Luke's Dictionary Querying Program!\n"
                  "----------------------------------------------")
            while True:
                try:
                    user_input = input("----------------------------------------------\n"
                                       "Please type the word you want to query(or exitprogram to quit):")
                    if user_input == "exitprogram":
                        print("\nThanks for using my dictionary! ^ ^\n"
                              "Your queries has been saved in ")
                        Dictionary.save_queries(queries, file_name=output_file)
                        return None

                    definition = dictionary.query_definition(user_input)
                    for index, mean in enumerate(definition):
                        print(f"{index + 1}: {mean}")
                    queries[user_input] = definition
                except NoSuchWordError as error:
                    print(error)
                    print("We can't find a word to match %s in our match system!" % error.word)
                except KeyError as error:
                    print(error, "from the match word is not existed in the dictionary!")
        except InvalidFileTypeError as error:
            print("This file extension %s is not belonging to .json or .txt" % error)


class UnInitializationError(Exception):
    """
    This exception would raise if user queries the word before loading dictionary.
    """
    def __init__(self) -> None:
        """
        Initialize the UnInitialize dictionary error.
        """
        super().__init__("You can not query a word without calling load_dictionary method!")


class NoSuchWordError(Exception):
    """
    This exception would raise if the match word function doesn't find a best closed word for the specific word.
    """
    def __init__(self, word: str = None) -> None:
        """
        Initialize the UnInitialize dictionary error.
        """
        self.word = word
        super().__init__("This word %s is not existed!" % word)


def main():
    dictionary = Dictionary()
    dictionary.querying_words_from_dictionary()


if __name__ == '__main__':
    main()