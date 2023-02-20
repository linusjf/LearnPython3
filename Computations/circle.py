#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import linspace, log
from math import pi
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("circle.pdf")
print("Setup Complete")

r = linspace(1, 100, 100)
C = 2 * pi * r
A = pi * r**2

plt.plot(r, C)
plt.xlabel("Radius of circle")
plt.ylabel("Circumference")
pp.savefig()
plt.clf()
plt.xlabel("Radius of circle")
plt.ylabel("Area")
plt.plot(r, A)
pp.savefig()
pp.close()
