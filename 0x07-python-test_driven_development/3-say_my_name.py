#!/usr/bin/python3
"""Defines the function to print first & last name"""


def say_my_name(first_name, last_name=""):
    """
    Prints or returns a message with the given first and last name.

    :param first_name: The first name (string).
    :param last_name: The last name (string, default is an empty string).
    :raises TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
