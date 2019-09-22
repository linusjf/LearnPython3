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

def main():
    """ exercise the class methods """
    _c = MyClass()
    _c.method1()
    _c.method2("Testing is fun")

if __name__ == "__main__":
    main()
