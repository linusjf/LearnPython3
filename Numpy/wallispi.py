#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import reduce

pi = 2 * reduce(lambda x, y: x * y,
                [float((4 * i ** 2) / (4 * i ** 2 - 1))
                 for i in range(1, 100000)])
print(pi)
