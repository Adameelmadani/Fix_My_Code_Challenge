#!/usr/bin/python3
"""
User class
"""


class User():
    """ This is our class """

    def __init__(self):
        """ The constructor """
        self.__email = None

    @property
    def email(self):
        """ Getter of email """
        return self.__email

    @email.setter
    def email(self, value):
        """ Setter of email """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
