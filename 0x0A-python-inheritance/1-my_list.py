#!/usr/bin/python3
""" inheritance"""


class MyList(list):
    """inheret list class"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
