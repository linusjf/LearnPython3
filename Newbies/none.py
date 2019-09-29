#!/usr/bin/env python3
"""Testing none."""


# pylint: disable=too-few-public-methods
class Foo():
    """Class Foo."""

    def __nonzero__(self):
        """Return interpretation of nonzero."""
        print('Foo is evaluated to a boolean!')
        return True
# pylint: enable=too-few-public-methods


X = None
print("X is None")
if X:
    print('if x')
if X is not None:
    print('if x is not None')
X = []
print("X is []")
if X:
    print('if x')
if X is not None:
    print('if x is not None')
X = 42
print("X is 42")
if X:
    print('if x')
if X is not None:
    print('if x is not None')
X = Foo()
print("X is Foo()")
if X:
    print('if x')
if X is not None:
    print('if x is not None')
