#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square.

        Args:
            size (int, optional): The size of the square.
            position (tuple, optional): The position of the square.

        Raises:
            TypeError: If size is not an integer or position is not a tuple
            ValueError: If size is less than 0 or position contains non-positive integers
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self._position

    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
            value (tuple): The position to set.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(i, int) for i in value) or \
           not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.size ** 2

    def my_print(self):
        """Prints the square with the character #."""
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)


if __name__ == "__main__":
    # Example usage
    my_square = Square(5, (0, 0))
    my_square.my_print()

    print("--")

    my_square = Square(5, (4, 1))
    my_square.my_print()

