#!/usr/bin/python3
# a class rectangle with private instance attributr 'width' and 'height'

"""
define class 'Rectangle'
"""


class Rectangle:
    """
    rectangle class with private instance attributes width & height
    """
    def __init__(self, width=0, height=0):
        """
           Args:
                width(int): width of the new rectangle
                height(int): height of new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        get width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        validates width as a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self, value):
        """
        validates height as a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

    def area(self):
        """
        Return:
            area of rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Return:
            perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.width * 2) + (self.__height * 2))
