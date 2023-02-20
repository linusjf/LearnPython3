#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

x = np.linspace(-5, 5, 101)
x_ = np.linspace(-5, 5, 31)


def f(x):
    return -np.exp(-(x**2))


# A smooth function
plt.figure(1, figsize=(3, 2.5))
plt.clf()

plt.plot(x_, f(x_) + 0.2 * np.random.normal(size=31), linewidth=2, c="g")
plt.plot(x, f(x), linewidth=2, c="r")

plt.ylim(ymin=-1.3)
plt.axis("off")
plt.tight_layout()
plt.savefig("noisy.png")
plt.savefig("noisy.pdf")
