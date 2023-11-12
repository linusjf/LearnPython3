#!/usr/bin/env python
"""
Ripple.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : ripple
# @created     : Sunday Nov 12, 2023 13:53:26 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("ripple.pdf")
print("Setup Complete")

x = np.linspace(-1, 1, 500)
X, Y = np.meshgrid(x, x)

ripple = np.sin((20 * X ** 2) + (20 * Y ** 2))
plt.imshow(ripple)

pp.savefig()
plt.imshow(ripple, cmap="gray")
pp.savefig()
pp.close()
