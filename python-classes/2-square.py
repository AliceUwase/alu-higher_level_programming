#!/usr/bin/python3
"""
    define a square
"""


class Square:
    """
    a class that defines square by its size
    """
    def __init__(self, size=0):
        """
        initializing the size of square


        Args:
            size(int):size of the square
        """

    if not isinstance(size, int):
        raise TypeError("size is must integer")
    elif size < 0:
        raise ValueError("size must ne >= 0")
    self.__size = size
