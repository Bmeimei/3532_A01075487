# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/11 14:34 
# File Name:        hypotenuse.py
from math import sqrt


def CalculateHypotenuse(first_side: int, second_side: int) -> float:
    """ Calculate the hypotenuse for two numbers.

    :param first_side: first number as an int
    :param second_side: second number as an int
    :return: hypotenuse as a float
    """
    return sqrt(first_side ** 2 + second_side ** 2)


def Sum(first: int, second: int) -> float:
    """ Calculate the Sum for two numbers.

    :param first: first number as an int
    :param second: second number as an int
    :return: sum as a float
    """
    return first + second


def Multiply(first: int, second: int) -> float:
    """ Calculate the Multiply for two numbers.

    :param first: first number as an int
    :param second: second number as an int
    :return: multiply as a float
    """
    return first * second


def Divide(first: int, second: int) -> float:
    """ Calculate the Divide for two numbers.

    :param first: first number as an int
    :param second: second number as an int
    :return: divide as a float
    """
    return first / second


def Subtract(first: int, second: int) -> float:
    """ Calculate the Subtract for two numbers.

    :param first: first number as an int
    :param second: second number as an int
    :return: subtract as a float
    """
    return first - second


def main() -> None:
    operator_dict = {"1": CalculateHypotenuse, "2": Sum, "3": Subtract, "4": Multiply, "5": Divide}
    print("1 to calculate hypotenuse")
    print("2 to add")
    print("3 to subtract")
    print("4 to multiply")
    print("5 to divide")
    operator = input()
    if operator not in operator_dict:
        print("Invalid Operator!")
    else:
        first = input("enter first number:")
        second = input("enter second number:")
        print(operator_dict.get(operator)(int(first), int(second)))


if __name__ == '__main__':
    main()