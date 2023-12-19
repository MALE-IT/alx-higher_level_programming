#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """Defines a square."""
    
    def __init__(self, size=0):
        """Initializes a new square.
        Args:
            size (int): The size of each side of the square (default is 0).
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
