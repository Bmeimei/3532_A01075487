# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/18 13:49 
# File Name:        asteroid.py

from vector import Vector
from random import randint
from math import pi


class Asteroid:
    """
    An Asteroid that has circumference, position and velocity.
    """

    def __init__(self, circumference: float, position: Vector, velocity: Vector) -> None:
        """
        Constructs an Asteroid.

        :param circumference: a positive float that represents the circumference of Asteroid
        :param position: a 3D vector that represents the position of Asteroid
        :param velocity: a 3D vector that represents the velocity of Asteroid
        :precondition: metres must be a positive int, position and velocity must be a vector
        """
        self.__circumference = circumference
        self.__position = position
        self.__velocity = velocity
        self.__id = self.__pass_id()
        self.__increment_id()

    """
    A unique id that represents the number of Asteroid. In other word,
    this id is the number of total Asteroid that has been initialized.
    The id would increase one whenever a new Asteroid has been created.
    """
    _id = 1

    @classmethod
    def __pass_id(cls) -> int:
        """
        Passes the unique id for current Asteroid.

        :return: a positive int as the unique Asteroid id
        """
        return cls._id

    @staticmethod
    def __increment_id() -> None:
        """
        The static method to add one for id when a new Asteroid has been created.
        """
        Asteroid._id += 1

    def get_id(self) -> int:
        """
        Returns the unique id for this asteroid.

        :return: An unique id as an int of this asteroid
        """
        return self.__id

    @staticmethod
    def random_asteroid() -> "Asteroid":
        """
        A static method that constructs a random asteroid. \n
        The radius of Asteroids would be in range [1, 4]. \n
        The three numbers in the position of Asteroids would be in range [0, 100]. \n
        The three numbers in the velocity of Asteroid would be in range [0, 5].

        :return: a new asteroid that made by random parameters.
        """
        lower_radius = 1
        upper_radius = 4
        lower_position_velocity = 0
        upper_position = 100
        upper_velocity = 5
        radius = randint(lower_radius, upper_radius)

        circumference = 2 * pi * radius
        position = Vector.random_vector(lower_position_velocity, upper_position)
        velocity = Vector.random_vector(lower_position_velocity, upper_velocity)
        return Asteroid(circumference, position, velocity)

    def get_circumference(self) -> float:
        """
        Getter for circumference.

        :return: metres as a positive float
        """
        return self.__circumference

    def get_position(self) -> tuple:
        """
        Getter for position

        :return: a 3D vector that represents the position of Asteroid
        """
        return self.__position.get_vector()

    def get_velocity(self) -> tuple:
        """
        Getter for velocity

        :return: a 3D vector that represents the velocity of Asteroid
        """
        return self.__velocity.get_vector()

    def set_circumference(self, circumference: float) -> None:
        """
        Setter for circumference.

        :param circumference: a positive float that replaces the old metres
        """
        self.__circumference = circumference

    def set_position(self, position: Vector) -> None:
        """
        Setter for position.

        :param position: a new Vector that replaces the old position
        """
        self.__position = position

    def set_velocity(self, velocity: Vector) -> None:
        """
        Setter for velocity.

        :param velocity: a new Vector that replaces the old velocity
        """
        self.__velocity = velocity

    @property
    def property_metres(self) -> property:
        """
        Property for getting or setting metres.

        :return: A property of getter and setter for metres
        """
        return property(self.get_circumference, self.set_circumference)

    @property
    def property_position(self) -> property:
        """
        Property for getting or setting position.

        :return: A property of getter and setter for position
        """
        return property(self.get_position, self.set_position)

    @property
    def property_velocity(self) -> property:
        """
        Property for getting or setting velocity.

        :return: A property of getter and setter for velocity
        """
        return property(self.get_velocity, self.set_velocity)

    def move(self) -> tuple:
        """
        Moves the Asteroid!

        :return: current position for asteroid as a tuple
        """
        self.__position.add(self.__velocity)
        return self.get_position()

    def __str__(self) -> str:
        """
        Returns the Asteroid's information in a string.

        :return: the information of Asteroid as a string
        """
        return "Metres: %d, Position: %s, Velocity: %s" % (self.__circumference, self.__position, self.__velocity)