#!/usr/bin/env python
# -*- coding: utf-8 -*-

# the tidy way
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('matplots.pdf')
print("Setup Complete")
#1D plotting:
x = np.linspace(0, 3, 20)
y = np.linspace(0, 9, 20)
# line plot
plt.plot(x, y)
pp.savefig()
plt.clf()
# dot plot
plt.plot(x, y, 'o')
pp.savefig()
plt.clf()

image = np.random.rand(30, 30)
plt.imshow(image, cmap=plt.cm.hot)
plt.colorbar()
pp.savefig()
plt.clf()

pp.close()
