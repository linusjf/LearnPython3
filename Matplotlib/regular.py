#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("regular.pdf")
print("Setup Complete")

n = 256
X = np.linspace(-np.pi, np.pi, n)
Y = np.sin(2 * X)
Y1 = Y + 1
Y2 = Y - 1
plt.plot(X, Y1, color="blue", alpha=1.00)
plt.fill_between(X, 1, Y1, facecolor="blue")
plt.plot(X, Y2, color="blue", alpha=1.00)
plt.fill_between(X, -1, Y2, where=Y2 >= -1, facecolor="blue")
plt.fill_between(X, -1, Y2, where=Y2 <= -1, facecolor="pink")
pp.savefig()
pp.close()
