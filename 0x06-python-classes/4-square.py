#!/usr/bin/python3
"""Square module."""

class Square:
    """Defines a square.

    Attributes:
        _size (int): Length of a side of the square.
    """

    def __init__(self, size=0):
        """Constructor.

        Args:
            size (int, optional): Length of a side of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self._size = size

    @property
    def size(self):
        """Property for the length of a side of this square.

        Returns:
            int: The length of a side of the square.
        """
        return self._size

    @size.setter
    def size(self, value):
        """Setter for the length of a side of this square.

        Args:
            value (int): The length of a side of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self._size = value
