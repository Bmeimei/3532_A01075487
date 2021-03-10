"""
This module is responsible for holding a badly written (but not so bad
that you won't find this in the workplace) BookAnalyzer class that needs
to be profiled and optimized.
"""


class BookAnalyzer:
    """
    This class provides the ability to load the words in a text file in
    memory and provide the ability to filter out the words that appear
    only once.
    """

    # a constant to help filter out common punctuation.
    COMMON_PUNCTUATION = ",*;.:([])"

    def __init__(self):
        self.text = None

    def read_data(self, src="House of Usher.txt"):
        """
        Reads through a text file and loads in all the words. This
        function also processes the words such that all whitespace and
        common punctuation is removed.
        :param src: the name of the file, a string
        """
        with open(src, mode='r', encoding='utf-8') as book_file:
            self.text = []
            temp = map(str.split, (line for line in book_file.readlines()))
            for i in temp:
                self.text += i
        for punctuation in self.COMMON_PUNCTUATION:
            self.text = [word.replace(punctuation, '') for word in self.text]

    def find_unique_words(self):
        """
        Filters out all the words in the text.
        Using set comprehension can get the unique word very fast.

        :return: a set of all the unique words.
        """
        return {unique_words.lower() for unique_words in self.text}


def main():
    book_analyzer = BookAnalyzer()
    book_analyzer.read_data()
    unique_words = book_analyzer.find_unique_words()
    print("--------------------------------------------------")
    print(f"List of unique words (Count: {len(unique_words)})")
    print("--------------------------------------------------")
    for word in unique_words:
        print(word)
    print("--------------------------------------------------")


if __name__ == '__main__':
    main()
