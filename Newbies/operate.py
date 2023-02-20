#!/usr/bin/env python3
"""Operator."""

import operator

ACTION = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
    "**": pow,
}
print(ACTION["-"](50, 25))
print(ACTION["+"](50, 25))
print(ACTION["/"](50, 25))
print(ACTION["*"](50, 25))
print(ACTION["**"](50, 25))
