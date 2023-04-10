#!/usr/bin/python3
"""raises exception"""


class BaseGeometry:
    """raises exception with message"""
    def area(self):
        raise Exception("area() is not implemented")
