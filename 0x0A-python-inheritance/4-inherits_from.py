#!/usr/bin/python3
"""Defines function that checks object is an instance of class"""


def inherits_from(obj, a_class):
    """Checks obj instance of class & inherited directly or indirectly."""
    return issubclass(type(obj), a_class)
