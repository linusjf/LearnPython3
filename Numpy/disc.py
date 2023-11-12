#!/usr/bin/env python
"""
Disc.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : disc
# @created     : Sunday Nov 12, 2023 08:16:51 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("disc.pdf")
print("Setup Complete")

x = np.linspace(-1, 1, 500)
print(x)
X, Y = np.meshgrid(x, x)
print(X)
print(Y)

RADIUS = 0.5
disc = (X ** 2) + (Y ** 2) < RADIUS ** 2
print(disc)
plt.imshow(disc, cmap="gray")

pp.savefig()
pp.close()
