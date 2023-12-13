#!/usr/bin/python3
<<<<<<< HEAD
"""Adds two numbers"""


def add_integer(a, b=98):
    """
    Returns sum of a and b
    - Args :
        a: int or float
        b: int or float, default 98
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")

    return a + b
=======
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """This function adds two integers

    :param a:The first integer
    :type a: int
    :param b: The second integer whose default value is 98
    :type b: int
    :returns: The addition of a and b
    :rtype: int
    :Raises: TypeError if either a or b is not an integer and not a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
>>>>>>> 9f087e22181279d64e0af95ddff9b0f71fb1e5fb
