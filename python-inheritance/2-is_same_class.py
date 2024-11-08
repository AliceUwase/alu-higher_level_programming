#!/usr/bin/python3
# a function that returns True if the object is exactly an instance 
""" a function that validates the object"""


def is_same_class(obj, a_class):
    """
        check if an object is an exact instance
        Return: - True
                - False
    """
    if type(obj) == a_class:
        return True
    return False
