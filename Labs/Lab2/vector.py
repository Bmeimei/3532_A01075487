# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/18 13:59 
# File Name:        vector.py

from random import randint


class Vector:
    """
    A three-dimension vector made by three integers.
    """

    def __init__(self, x: int, y: int, z: int) -> None:
        """
        Constructs the three-dimension Vector.

        :param x: x-axis as an int
        :param y: y-axis as an int
        :param z: z-axis as an int
        :precondition: x, y, z must be an int
        """
        self.__x = x
        self.__y = y
        self.__z = z

    @staticmethod
    def random_vector(lower_bound: int = 0, upper_bound: int = 100) -> "Vector":
        """
        A static method that constructs a random vector.
        x, y, z are all in range [lower_bound, upper_bound].
        Default value for lower_bound is 0, and for upper_bound is 100.

        :param lower_bound: The lower bound for random number as an int.
        :param upper_bound: The upper bound for random number as an int.
        :precondition: lower_bound must be smaller than upper_bound, and both of them must be an int.

        :return: A vector that made by random x, y and z
        """
        random_x = randint(lower_bound, upper_bound)
        random_y = randint(lower_bound, upper_bound)
        random_z = randint(lower_bound, upper_bound)
        return Vector(random_x, random_y, random_z)

    def get_vector(self) -> tuple:
        """
        Returns the vector as a tuple

        :return: the tuple that represents the vector, including x, y, and z axis
        """
        return self.__x, self.__y, self.__z

    def get_X(self) -> int:
        """
        Returns the x-axis
        :return: x-axis as an int
        """
        return self.__x

    def get_Y(self) -> int:
        """
        Returns the y-axis
        :return: y-axis as an int
        """
        return self.__y

    def get_Z(self) -> int:
        """
        Returns the z-axis
        :return: z-axis as an int
        """
        return self.__z

    def set_X(self, x: int) -> None:
        """
        Sets x-axis
        :param x: the new x-axis that replaces the old x-axis
        """
        self.__x = x

    def set_Y(self, y: int) -> None:
        """
        Sets y-axis
        :param y: the new y-axis that replaces the old y-axis
        """
        self.__y = y

    def set_Z(self, z: int) -> None:
        """
        Sets z-axis
        :param z: the new z-axis that replaces the old z-axis
        """
        self.__z = z

    def add(self, vector) -> None:
        """
        Adds another vector to this vector

        :param vector: the another vector that would be added into this vector
        """
        self.__x += vector.get_X()
        self.__y += vector.get_Y()
        self.__z += vector.get_Z()

    def __str__(self) -> str:
        """
        Returns the vector as a string

        :return: a string that represents the vector
        """
        return f"%{self.__x}, {self.__y}, {self.__z}"