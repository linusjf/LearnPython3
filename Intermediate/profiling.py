#!/usr/bin/env python3
"""Profiling example."""

import profile


class Test:
    """Test class."""

    def __init__(self):
        """Construct the object."""
        self.str = ""

    # pylint: disable=method-hidden
    def check(self, _a, _b, _c):
        """Repeat b 100 times in string."""
        self.str = _b * 100
        # ensures that above is run only once
        self.check = self.check_post
    # pylint: enable=method-hidden

    def check_post(self, _a, _b, _c):
        """Repeat c 100 times in string."""
        self.str = _c * 100


A = Test()


def example2():
    """Run check 100000 times."""
    for i in range(0, 100000):
        A.check(i, "b", "c")


profile.run("example2()")
