# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/25 15:07 
# File Name:        dvd.py

from library_item import LibraryItem


class DVD(LibraryItem):
    """
    DVD has a release date, and a region code.
    """

    def __init__(self, call_num: str, title: str, num_copies: int, release_date: str, region_code: str):
        super().__init__(call_num, title, num_copies)
        self._release_date = release_date
        self._region_code = region_code

    @property
    def release_date(self) -> str:
        """
        Gets the release date.
        """
        return self._release_date

    @property
    def region_code(self) -> str:
        """
        Gets the region code.
        """
        return self._region_code

    def __str__(self) -> str:
        """
        DVD String.
        """
        return f"---- DVD: {self.title} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self.num_copies}\n" \
               f"Release Date: {self.release_date}" \
               f"Region Code: {self.region_code}"
