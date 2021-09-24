#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def f(x):
    return x**2 + 10*np.sin(x)

x = np.arange(-10, 10, 0.1)
plt.plot(x, f(x))
plt.savefig("minimize.png")
plt.savefig("minimize.pdf")

result = optimize.minimize(f, x0=0)
print(result)
print(f"Solution converges to {result.x}")

result = optimize.minimize(f, x0=0, method="L-BFGS-B")
print(result)
print(f"Solution converges to {result.x}")

result = optimize.minimize(f, x0=3, method="L-BFGS-B")
print(result)
print(f"Solution converges to {result.x}")

result = optimize.basinhopping(f, 0)  
print(result)
print(f"Solution converges to {result.x}")

result = optimize.minimize(f, x0=1,
                        bounds=((0, 10), ))
print(result)
print(f"Solution converges to {result.x}")
