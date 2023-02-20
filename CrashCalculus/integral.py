#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("integral.pdf")
print("Setup Complete")


def f(x):
    return 2 * x


# Set up x from -10 to 10 with small steps
delta_x = 0.1
x = np.arange(-10, 10, delta_x)
# Find f(x) * delta_x
fx = f(x) * delta_x
# Compute the running sum
y = fx.cumsum()
# Plot
plt.plot(x, y)
plt.title("Integral of 2x")
pp.savefig()
pp.close()
