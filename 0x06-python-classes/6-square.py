#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Defines a square."""
    
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square.
        
        Args:
            size (int): The size of the new square (default is 0).
            position (tuple): The position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.
        
        Args:
            value (int): The size of the square.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.
        
        Args:
            value (tuple): The position of the square.
        
        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value) or \
                not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the current square area."""
        return self.__size ** 2
    def my_print(self):
    """Prints the square with the # character."""
    if self.__size == 0:
        print("")
        return

    [print("") for i in range(0, self.__position[1])]

    for i in range(0, self.__size):
        [print(" ", end="") for j in range(0, self.__position[0])]
        [print("#", end="") for k in range(0, self.__size)]
        print("")
