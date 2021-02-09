# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/2/9 0:10
# File Name:        test_dictionary.py
from unittest import TestCase
from dictionary import Dictionary, UnInitializationError, NoSuchWordError
from file_handler import FileHandler, InvalidFileTypeError
from difflib import Differ
from file_extensions import FileExtensions


class TestDictionary(TestCase):
    """
    - Loading data into a dictionary.
    - Writing data to a text file.
    - Querying a word.
    """

    def test_dictionary_without_loading(self):
        """Test if the dictionary is None in Dictionary before loading it."""
        dictionary = Dictionary()
        self.assertEqual(dictionary.dictionary, None)

    def test_dictionary_after_loading(self):
        """Test if the dictionary is a dict in Dictionary after loading it."""
        dictionary = Dictionary()
        dictionary.load_dictionary()
        self.assertEqual(type(dictionary.dictionary), dict)

    def test_dictionary_with_not_exist_path(self):
        """Test dictionary after loading with a not existed path."""
        dictionary = Dictionary()
        self.assertRaises(FileNotFoundError, dictionary.load_dictionary, "not_exist")

    def test_load_dictionary_with_wrong_file_extension(self):
        """Test dictionary with wrong file extension."""
        dictionary = Dictionary()
        self.assertRaises(InvalidFileTypeError, dictionary.load_dictionary, "data.json", 3)

    def test_query_definition_without_loading(self):
        """Test querying definition without loading dictionary."""
        dictionary = Dictionary()
        self.assertRaises(UnInitializationError, dictionary.query_definition, "Hello")

    def test_query_definition_with_none(self):
        """Test querying definition with None."""
        dictionary = Dictionary()
        dictionary.load_dictionary()
        word = None
        self.assertRaises(TypeError, dictionary.query_definition, word)

    def test_query_definition_with_empty_string(self):
        """Test querying definition with empty string."""
        dictionary = Dictionary()
        dictionary.load_dictionary()
        word = ""
        self.assertRaises(NoSuchWordError, dictionary.query_definition, word)

    def test_query_definition_with_nonsense_word(self):
        """Test querying definition with empty string."""
        dictionary = Dictionary()
        dictionary.load_dictionary()
        word = "asddsaasdadsadsdsadassdaasd"
        self.assertRaises(NoSuchWordError, dictionary.query_definition, word)

    def test_query_definition_with_not_match_word(self):
        """Test querying definition with a not matched string."""
        dictionary = Dictionary()
        dictionary.load_dictionary()
        word = "gagoola"
        self.assertRaises(KeyError, dictionary.query_definition, word)

    def test_query_definition_with_rain(self):
        """Test querying definition with input rain."""
        dictionary = Dictionary()
        dictionary.load_dictionary()
        word = "rain"
        self.assertEqual(dictionary.query_definition(word), ['Precipitation in the form of liquid water drops with'
                                                             ' diameters greater than 0.5 millimetres.',
                                                             'To fall from the clouds in drops of water.'])

    def test_query_definition_with_close_word(self):
        """Test querying definition with close word."""
        dictionary = Dictionary()
        dictionary.load_dictionary()
        word = "RaInn"
        self.assertEqual(dictionary.query_definition(word), ['Precipitation in the form of liquid water drops with'
                                                             ' diameters greater than 0.5 millimetres.',
                                                             'To fall from the clouds in drops of water.'])

    def test_load_data_after_saving_queries(self):
        """Test loading data with a not existed path."""
        dictionary = Dictionary()
        dictionary.load_dictionary()
        queries = {"hello": ["Expression of greeting used by two or more people who meet each other."]}
        path = "saved_queries.txt"
        dictionary.save_queries(queries)
        expected = FileHandler.load_data(path, FileExtensions.TXT)
        self.assertTrue("hello" in expected)

    def test_not_exist_word_not_in_saving_queries(self):
        """Test loading data with a not existed path."""
        path = "saved_queries.txt"
        expected = FileHandler.load_data(path, FileExtensions.TXT)
        self.assertTrue("dsadsadsadsaasdads" not in expected)

    def test_save_queries(self):
        """Test saving queries into a file after clearing the file."""
        dictionary = Dictionary()
        dictionary.load_dictionary()
        queries = {"hello": ["Expression of greeting used by two or more people who meet each other."]}
        path = "saved_queries.txt"
        with open(path, "w") as write_file:
            write_file.write("")
        with open(path, "r") as first_file:
            before_save = first_file.read().split()
        dictionary.save_queries(queries)
        with open(path, "r") as second_file:
            after_save = second_file.read().split()
        differ = Differ()
        self.assertEqual("".join(differ.compare(before_save, after_save)),
                         '+ {"hello":+ ["Expression+ of+ greeting+ used+ by+ two+ or+'
                         ' more+ people+ who+ meet+ each+ other."]}')