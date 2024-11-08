#!/usr/bin/python3
# a function that returns the list of available attributes and methods of an object
"""define 'lookup' function"""


def lookup(obj):
    """Return:list object"""
    return dir(obj)
