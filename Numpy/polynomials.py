#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('polynomials.pdf')
print("Setup Complete")

p = np.poly1d([3, 2, -1])
print(p(0),p.roots,p.order)

x = np.linspace(0, 1, 20)
y = np.cos(x) + 0.3*np.random.rand(20)
p = np.poly1d(np.polyfit(x, y, 3))
# use a larger number of points for smoother plotting
t = np.linspace(0, 1, 200) 
plt.plot(x, y, 'o', t, p(t), '-')

pp.savefig()
plt.clf()

# coefs in different order!
p = np.polynomial.Polynomial([-1, 2, 3]) 
print(p(0),p.roots())
# In general polynomials do not always expose 'order'
print(p.degree())
x = np.linspace(-1, 1, 2000)
y = np.cos(x) + 0.3*np.random.rand(2000)
p = np.polynomial.Chebyshev.fit(x, y, 90)
plt.plot(x, y, 'r.')
plt.plot(x, p(x), 'k-', lw=3)

pp.savefig()
plt.clf()
pp.close()
