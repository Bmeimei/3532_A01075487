# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/11 14:34 
# File Name:        hypotenuse.py
from math import sqrt


def CalculateHypotenuse(first_side: int, second_side: int) -> float:
    """
    Calculates the length of the hypotenuse when given
    two arguments that are the lengths of the sides of a right angle triangle.

    :param first_side: an int that represents one side
    :param second_side: an int that represents another side
    :precondition: first_side must be an int
    :precondition: second_side must be an int
    :return: hypotenuse as a float
    """
    return sqrt(first_side ** 2 + second_side ** 2)


def main():
    first_value = input("Please input the first value: ")
    second_value = input("Please input the second value: ")
    print("Result:", CalculateHypotenuse(int(first_value), int(second_value)))


if __name__ == '__main__':
    main()