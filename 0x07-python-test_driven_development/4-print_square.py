#!/usr/bin/python3

def print_square(size):
    """
    Prints a square of '#' characters.

    :param size: The size length of the square.
    :raises TypeError: If size is not an integer.
    :raises ValueError: If size is less than 0.
    :raises TypeError: If size is a float and is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float):
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)

if __name__ == "__main__":
    # Example usage
    print_square(4)


