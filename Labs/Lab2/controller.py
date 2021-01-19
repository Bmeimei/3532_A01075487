# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/18 16:49 
# File Name:        controller.py

from asteroid import Asteroid
from time import sleep
from datetime import datetime
from math import ceil


class Controller:
    """
    A controller that has many Asteroid to play.
    """

    def __init__(self) -> None:
        """
        Constructs a new controller with 100 asteroids.
        Asteroids are in a cube with 100 * 100 * 100 metres.
        The radius of Asteroids would be in range [1, 4].
        The three numbers in the position of Asteroids would be in range [0, 100].
        The three numbers in the velocity of Asteroid would be in range [0, 5].
        """
        self.asteroids_list = [Asteroid.random_asteroid() for _ in range(100)]

    @staticmethod
    def string_of_element_in_tuple_without_parentheses(target: tuple) -> str:
        """
        Returns a formatted string that represents the elements in a tuple without parentheses.

        :param target: the target tuple
        :return: a string of tuple elements
        >>> Controller.string_of_element_in_tuple_without_parentheses((1, 2, 3))
        '1, 2, 3'
        >>> Controller.string_of_element_in_tuple_without_parentheses((10, 2))
        '10, 2'
        """
        return "".join(map(lambda x: str(x) + ", ", target))[0: -2]

    def simulate(self, seconds: int) -> None:
        """
        Let's play asteroid!

        :param seconds: an int of seconds that represents the times of moving for asteroids
        :precondition: seconds must be a positive int
        """
        while seconds > 0:
            current_time = datetime.now()
            time_stamp = current_time.timestamp()
            sleep(ceil(time_stamp) - time_stamp)
            start_time = datetime.now()
            print("Simulation Start Time:", start_time)
            print("Moving Asteroids!\n"
                  "----------------")
            for asteroid in self.asteroids_list:
                print("Asteroid %d Moved! Old Pos: %s -> New Pos: %s" %
                      (asteroid.get_id(),
                       self.string_of_element_in_tuple_without_parentheses(asteroid.get_position()),
                       self.string_of_element_in_tuple_without_parentheses(asteroid.move())))
                print("Asteroid %d is currently at %s and moving at %s metres per second. "
                      "It has a circumference of %s" %
                      (asteroid.get_id(),
                       self.string_of_element_in_tuple_without_parentheses(asteroid.get_position()),
                       self.string_of_element_in_tuple_without_parentheses(asteroid.get_velocity()),
                       asteroid.get_circumference()))
            print()
            seconds -= 1


def main() -> None:
    """
    Drive!
    """
    controller = Controller()
    controller.simulate(10)


if __name__ == '__main__':
    main()
