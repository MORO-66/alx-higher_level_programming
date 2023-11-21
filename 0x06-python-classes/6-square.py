#!/usr/bin/python3
"""3-square.py."""


class Square:
    """A class representing a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size
        self.position = position
    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
