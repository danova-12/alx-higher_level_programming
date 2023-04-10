#!/usr/bin/python3
"""module"""


def add_attribute(obj, name, value):
    """Assigns new attributes if not already assigned
        Args:
            name (str): name of the attribute to insert
            value (any): value of the attribute to insert
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
