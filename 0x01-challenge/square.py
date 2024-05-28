#!/usr/bin/python3
""" Module of square class """


class square():
    """ Square Class """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Initializes a new instance of the Square class """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ The perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Returns a string representation of the square, showing its
        dimensions """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Create a Square object """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
