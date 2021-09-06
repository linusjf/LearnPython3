#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import linspace
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('ball_plot.pdf')
print("Setup Complete")

v0 = 5
g = 9.81
t = linspace(0, 1, 1001)

y = v0*t - 0.5*g*t**2

plt.plot(t, y)
plt.xlabel('t (s)')
plt.ylabel('y (m)')
plt.show()
pp.savefig()
pp.close()
