#!/usr/bin/python3
"""
    2-rectangle: class.
"""


class Rectangle:
    """
        class Rectangle defines a rectangle
        Attributes:
            width (int): width of the r
            height (int): heighttangle
    """
    def __init__(self, width=0, height=0):
        """
            initialises the instances
            Args:
                width (int): widt
                height (int): height of
        """
        if isinstance(width, int):
            if width < 0:
                raise ValueError("width must be >= 0")
            self.__width = width
        else:
            raise TypeError("width must be an integer")

        if isinstance(height, int):
            if height < 0:
                raise ValueError("height must be >= 0")
            self.__height = height
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """
            getter function for pth
            Retruns: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            setter function for private attribute width
            Args:
                value (int): new widthe
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            getter function for privateheight
            Returns: heig
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            setter function for the privaribute height
            Args:
                value (int): new height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            public instance method area of rectangle
            Returns: area of rect
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            public instance method to calcperimeter of a rectangle
            Returns: perimete
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__width + self.__height)
