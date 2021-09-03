#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('distance.pdf')
print("Setup Complete")

mileposts = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544,
                      1913, 2448])
distance_array = np.abs(mileposts - mileposts[:, np.newaxis])
print(distance_array)

x, y = np.arange(5), np.arange(5)[:, np.newaxis]
distance = np.sqrt(x ** 2 + y ** 2)
print(distance)
plt.pcolor(distance)
plt.colorbar()

pp.savefig()
plt.clf()

pp.close()

x, y = np.ogrid[0:5, 0:5]
print(x, y)
print(x.shape, y.shape)
distance = np.sqrt(x ** 2 + y ** 2)
x, y = np.mgrid[0:4, 0:4]
print(x)
print(y)
