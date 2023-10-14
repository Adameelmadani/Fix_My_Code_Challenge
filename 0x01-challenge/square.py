#!/usr/bin/python3
"""
This is our module
"""


class square():
    """
    This is our class
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """
        This is our constructor
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """
        Area of the square
        """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """
        Permiter of the square
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        string representation of square
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
