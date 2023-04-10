#!/usr/bin/python3
"""changes string represantition"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines a Square class"""
    def __init__(self, size):
        """instantiate and validate attribute
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
