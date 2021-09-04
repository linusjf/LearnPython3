#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

x = np.ma.array([1, 2, 3, 4], mask=[0, 1, 0, 1])
print(x)
y = np.ma.array([1, 2, 3, 4], mask=[0, 1, 1, 1])
print(x + y)
print(np.ma.sqrt([1, -1, 2, -2]))
