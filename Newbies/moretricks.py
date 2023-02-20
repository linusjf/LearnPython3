#!/usr/bin/env python3
"""More python tricks."""
import sys

# Use Of Ternary Operator For Conditional
# Assignment.


def small(_a, _b, _c):
    """Return smallest number."""
    return _a if _a <= _b and _a <= _c else (_b if _b <= _a and _b <= _c else _c)


print(small(1, 0, 1))
print(small(1, 2, 2))
print(small(2, 2, 3))
print(small(5, 4, 3))

VECTOR = [m**2 if m > 10 else m**4 for m in range(50)]
print(VECTOR)

# Multi-line strings
MULTI_STR = "select * from multi_row \
where row_id < 5"
print(MULTI_STR)

MULTI_STR = """select * from multi_row
where row_id < 5"""
print(MULTI_STR)

MULTI_STR = "select * from multi_row " "where row_id < 5 " "order by age"
print(MULTI_STR)

# Dictionary/Set Comprehensions.
TEST_DICT = {i: i * i for i in range(10)}
TEST_SET = {i * 2 for i in range(10)}

print(TEST_SET)
print(TEST_DICT)

# inspect object in python3
TEST = [1, 3, 5, 7]
print(dir(TEST))

# Detect Python Version At Runtime.


# Detect the Python version currently in use.
if not sys.version_info >= (3, 5):
    print("Sorry, you aren't running on Python 3.5\n")
    print("Please upgrade to 3.5.\n")
    sys.exit(1)

# Print Python version in a readable format.
print("Current Python version: ", sys.version)

# splat operator


def test(_x, _y, _z):
    """Just print."""
    print(_x, _y, _z)


TEST_DICT = {"_x": 1, "_y": 2, "_z": 3}
TEST_LIST = [10, 20, 30]

test(*TEST_DICT)
test(**TEST_DICT)
test(*TEST_LIST)

# dictionary of expressions

STDCALC = {
    "sum": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "product": lambda x, y: x * y,
    "division": lambda x, y: x / y,
    "power": lambda x, y: x**y,
    "nthroot": lambda x, y: x ** (1 / y),
}

print(STDCALC["sum"](9, 3))
print(STDCALC["subtract"](9, 3))
print(STDCALC["product"](9, 3))
print(STDCALC["division"](9, 3))
print(STDCALC["power"](9, 3))
print(STDCALC["nthroot"](9, 3))
print(STDCALC["power"](STDCALC["nthroot"](9, 3), 3))
