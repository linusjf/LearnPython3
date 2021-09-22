#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy.interpolate import interp1d
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import Rbf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('interpolate.pdf')
print("Setup Complete")

x = np.linspace(0, 4, 12)
y = np.cos(x**2/3+4)
print(x,y)

plt.plot(x, y,'o')
pp.savefig()
plt.clf()

f1 = interp1d(x, y,kind = 'linear')
f2 = interp1d(x, y, kind = 'cubic')

xnew = np.linspace(0, 4,30)

plt.plot(x, y, 'o', xnew, f1(xnew), '-', xnew, f2(xnew), '--')

plt.legend(['data', 'linear', 'cubic'], loc = 'best')

pp.savefig()
plt.clf()

x = np.linspace(-3, 3, 50)
y = np.exp(-x**2) + 0.1 * np.random.randn(50)
plt.plot(x, y, 'ro', ms = 5)

spl = UnivariateSpline(x, y)
xs = np.linspace(-3, 3, 1000)
plt.plot(xs, spl(xs), 'g', lw = 3)

spl.set_smoothing_factor(0.5)
plt.plot(xs, spl(xs), 'b', lw = 3)
plt.legend(['data', 'default', 'sf = 0.5'], loc = 'best')
pp.savefig()
plt.clf()


xs = np.linspace(-3, 3, 1000)
ys = xs**2 + np.sin(xs) + 1
interp_func = Rbf(xs, ys)
newx = np.arange(2, 3, 0.1)
plt.plot(xs, ys, 'g', lw = 3)
plt.scatter(newx, interp_func(newx),c='r')
plt.legend(['data', 'Rbf'], loc = 'best')
pp.savefig()

pp.close()
