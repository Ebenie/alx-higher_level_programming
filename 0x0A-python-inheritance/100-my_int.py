#!/usr/bin/python3
"""Defines the MyInt class"""


class MyInt(int):
    """MyInt class that inherits from int with inverted operators"""

    def __eq__(self, other):
        """The function defines the == operator and !="""
        return super().__ne__(other)

    def __ne__(self, other):
        """The function defines the != operator and =="""
        return super().__eq__(other)
