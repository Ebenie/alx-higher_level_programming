#!/usr/bin/python3
"""Writes a class MyList that inherits from list"""


class MyList(list):
    """A custom class that inherits from the list class"""

    def print_sorted(self):
        """The function Prints the lists in order"""
        sorted_list = sorted(self)
        print(sorted_list)
