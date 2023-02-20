#!/usr/bin/env python3
"""Sort dictionary."""
import operator
import json
from pprint import PrettyPrinter

XS = {"a": 4, "b": 3, "c": 2, "d": 1}

print(sorted(XS.items(), key=lambda x: x[1]))

# Or:

print(sorted(XS.items(), key=operator.itemgetter(1)))

XS = {
    "bash": "unix",
    "command": "windows",
    "powershell": "windows",
    "korn": "unix",
}
print(sorted(XS.items(), key=lambda x: x[0]))
print(sorted(XS.items(), key=lambda x: x[1]))

MAPPING = {"a": 23, "b": 42, "c": 0xC0FFEE}
print(json.dumps(MAPPING, indent=4, sort_keys=True))

# Note this only works with dicts containing
# primitive types (check out the "pprint" module):
try:
    json.dumps({all: "yup"})
except TypeError as type_error:
    print(type_error)

print("Pretty printing...")

PP = PrettyPrinter(indent=4, compact=False, width=10, depth=2)
PP.pprint(MAPPING)
PP.pprint({all: "yup"})
