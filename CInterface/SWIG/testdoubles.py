#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import cos_doubles

x = np.arange(0, 2 * np.pi, 0.1)
y = np.empty_like(x)

cos_doubles.cos_doubles_func(x, y)
plt.plot(x, y)
plt.savefig("testdoubles.png")

dir(cos_doubles)
x = np.array([1.0, 0.0, 3.14159265359])
y = np.empty_like(x)
cos_doubles.cos_doubles_func(x, y)
print(y)
