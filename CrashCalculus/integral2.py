#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("integral2.pdf")
print("Setup Complete")


def f(x):
    return 3 * x**2 - 4 * x


# Set up x from -10 to 10 with small steps
delta_x = 0.1
x = np.arange(-10, 10, delta_x)
# Find f(x) * delta_x
fx = f(x) * delta_x
# Compute the running sum
y1 = fx.cumsum()
y2 = x**3 - 2 * x**2
# Plot
plt.plot(x, y1, c="r", alpha=0.5, label="area")
plt.plot(x, y2, c="b", alpha=0.5, label="antiderivative")
plt.title("Integral of 3x² - 4x")
plt.legend()
pp.savefig()
pp.close()
