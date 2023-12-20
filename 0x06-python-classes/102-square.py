#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new square.

        Args:
            size (int or float, optional): The size of the square.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int or float): The size to set.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.size ** 2

    def __eq__(self, other):
        """Checks if two squares have equal area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Checks if two squares have different area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Checks if the area of the first square is less than the second square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Checks if the area of the first square is less than or equal to the second square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Checks if the area of the first square is greater than the second square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Checks if the area of the first square is greater than or equal to the second square."""
        return self.area() >= other.area()


if __name__ == "__main__":
    # Example usage
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")

