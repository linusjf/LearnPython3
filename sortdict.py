#!/usr/bin/env python3
"""Sort dictionary"""
import operator
XS = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

print(sorted(XS.items(), key=lambda x: x[1]))

# Or:

print(sorted(XS.items(), key=operator.itemgetter(1)))

XS = {"bash":"unix", "command":"windows", "powershell":"windows", "korn":"unix"}
print(sorted(XS.items(), key=lambda x: x[0]))
print(sorted(XS.items(), key=lambda x: x[1]))
