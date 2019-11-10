#!/usr/bin/env python
"""Counter."""

from collections import Counter

C = Counter('helloworld')

print(C)

print(C.most_common(3))
