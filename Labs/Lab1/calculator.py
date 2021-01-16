# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/15 23:16 
# File Name:        calculator.py.py
from hypotenuse import CalculateHypotenuse


def Add(first: int, second: int) -> float:
    """
    Calculates the Sum for two numbers.

    :param first: first number as an int
    :param second: second number as an int
    :precondition: first must be an int
    :precondition: second must be an int
    :return: sum as a float
    """
    return first + second


def Multiply(first: int, second: int) -> float:
    """
    Calculates the Multiply for two numbers.

    :param first: first number as an int
    :param second: second number as an int
    :precondition: first must be an int
    :precondition: second must be an int
    :return: multiply as a float
    """
    return first * second


def Divide(first: int, second: int) -> float:
    """
    Calculates the Divide for two numbers.

    :param first: first number as an int
    :param second: second number as an int
    :precondition: first must be an int
    :precondition: second must be an int
    :return: divide as a float
    """
    return first / second


def Subtract(first: int, second: int) -> float:
    """
    Calculates the Subtract for two numbers.

    :param first: first number as an int
    :param second: second number as an int
    :precondition: first must be an int
    :precondition: second must be an int
    :return: subtract as a float
    """
    return first - second


def main() -> None:
    operator_dict = {"1": CalculateHypotenuse, "2": Add, "3": Subtract, "4": Multiply, "5": Divide}
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