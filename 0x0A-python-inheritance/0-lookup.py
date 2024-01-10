#!/usr/bin/python3
"""Creates a function for inspecting object attributes"""


def lookup(obj):
    """Returns list of attributes & methods of an object"""
    return (dir(obj))
