#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import linspace, where
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("ball_plot.pdf")
print("Setup Complete")

v0 = 4.5
g = 9.81
t = linspace(0, 1, 1001)

y = v0 * t - 0.5 * g * t**2

y0 = where(y <= 0)
index = y0[0][1]
t0 = 0.5 * (t[index - 1] + t[index])
print("Time when ball hits ground = %g" % (t0))
plt.plot(t, y)
plt.xlabel("t (s)")
plt.ylabel("y (m)")
plt.show()
pp.savefig()
pp.close()
