#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import arange, pi, sin
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("plotsin.pdf")
print("Setup Complete")

x = arange(-pi, pi, 0.01)
y = sin(x) * sin(2 * x)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("sin(x)sin(2x)")
plt.show()
pp.savefig()

y = sin(2 * x) * sin(3 * x)
plt.xlabel("x")
plt.ylabel("sin(2x)sin(3x)")
plt.show()
pp.savefig()
pp.close()
