#!/usr/bin/env python3
""" Example of class definition"""
# Example file for working with classes


class MyClass():
    """ Class definition """

    # pylint: disable=no-self-use
    def method1(self):
        """ Method 1 """
        print("Guru99")

    def method2(self, some_string):
        """ Method 2 """
        print("Software Testing:" + some_string)
    # pylint: enable=no-self-use


class ChildClass(MyClass):
    """ Class definition """

    # pylint: disable=no-self-use
    def method1(self):
        """ Method 1 """
        print("Into method 1 of ChildClass")
        super().method1()

    def method2(self, some_string):
        """ Method 2 """
        print("Child class method 2:" + some_string)
    # pylint: enable=no-self-use

# pylint: disable=too-few-public-methods


class User:
    """ Class User definition """
    name = ""

    def __init__(self, name):
        """ Constructor """
        self.name = name

    def say_hello(self):
        """ Say hello method """
        print("Welcome to Guru99, " + self.name)
# pylint: enable=too-few-public-methods


def main():
    """ exercise the class methods """
    _c = MyClass()
    _c.method1()
    _c.method2("Testing is fun")
    _c = ChildClass()
    _c.method1()
    _c.method2("Testing is fun")
    user = User("Alex")
    user.say_hello()


if __name__ == "__main__":
    main()
