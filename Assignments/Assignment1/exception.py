# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/19 22:37 
# File Name:        exception.py

def check_type(target: object, *target_type: type) -> None:
    """
    Checks the target is in the target type tuple. Raises TypeError if not or target is None.

    :param target: the target that would be checked
    :param target_type: the target type tuple
    :raise TypeError: If target is not in the target type or target is None
    """
    if target is None:
        raise TypeError(target, "is None!")

    if not isinstance(target, target_type):
        raise TypeError(target, "is not a valid type in", target_type)


def check_all_input_type(target: list[object], *target_type: type) -> None:
    """
    Checks a bunch of inputs is one of the target type. Raises TypeError if one of the input is invalid type or None.
    :param target: a list that made by inputs.
    :param target_type: the target type tuple
    :raise TypeError: If one of the input target is not in the target type or target is None
    """
    for element in target:
        check_type(element, *target_type)


def check_value_is_lower_than_threshold(target: float, value: float) -> None:
    """
    Checks the number is over to the value. Raises ValueError if not.

    :param target: the number that would be checked
    :param value: the value that compares with target
    :raise ValueError: If the target is smaller than the value
    """
    if target < value:
        raise ValueError(target, "is smaller than the minimum value", value)


def check_value_is_lower_equal_than_threshold(target: float, value: float) -> None:
    """
    Checks the number is over or equal to the value. Raises ValueError if not.

    :param target: the number that would be checked
    :param value: the value that compares with target
    :raise ValueError: If the target is smaller than the value
    """
    if target <= value:
        raise ValueError(target, "is smaller or equal to the minimum value", value)


def check_all_input_value(target: list[float], value: float) -> None:
    """
    Checks a bunch of numbers is over or equal to the value. Raises ValueError if not.
    :param target: a list that made by a bunch of number inputs.
    :param value: the value that compares with target
    :raise TypeError: If one of the input target is not in the target type or target is None
    """
    for element in target:
        check_value_is_lower_than_threshold(element, value)


def check_string_is_empty(target: str) -> None:
    """
    Checks the input string is empty. Raises ValueError if it is.

    :param target: the input string
    :return: ValueError: If the target string is empty or only contains space.
    """
    if len(target.strip()) == 0:
        raise ValueError("The input is an empty string!")