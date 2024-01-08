#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    :param obj: The object to look up.
    :return: A list of attributes and methods.
    """
    return dir(obj)

