#!/usr/bin/python3
# a class that defines rectangle
"""
define rectangle
"""


class Rectangle:
    """
    Rectangle with private instance attributes: 'width' & 'height'
    """
    def __init__(self, width=0, height=0):
        """
        Args:
            width (int): width of the new rectangle
            height (int): height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Validate width as a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Validate height as a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
