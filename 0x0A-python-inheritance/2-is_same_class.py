#!/usr/bin/python3
"""check object is instance of class"""


def is_same_class(obj, a_class):
    """check using type"""
    return True if type(obj) is a_class else False
