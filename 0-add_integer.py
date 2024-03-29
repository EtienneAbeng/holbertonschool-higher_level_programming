#!/usr/bin:python3
''' Le script devra écrire une fonction qui ajoute 2 entier'''


def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
        a (int or float): The first number.
        b (int or float): The second number. Default is 98.

    Raises:
        TypeError: If a or b is not an integer or float.

    Returns:
        int: The sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

