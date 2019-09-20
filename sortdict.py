#!/usr/bin/env python3

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

print(sorted(xs.items(), key=lambda x: x[1]))

# Or:

import operator
print(sorted(xs.items(), key=operator.itemgetter(1)))

xs = {"bash":"unix", "command":"windows","powershell":"windows","korn":"unix"}
print(sorted(xs.items(), key=lambda x: x[0]))
print(sorted(xs.items(), key=lambda x: x[1]))
