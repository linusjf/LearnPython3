#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import linspace,log
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('volumecubes.pdf')
print("Setup Complete")

L = linspace(1, 500, 500)
V = L**3
plt.plot(L, V)
plt.xlabel('Length of side')
plt.ylabel('Volume')
pp.savefig()
plt.clf()
plt.plot(L, log(V))
plt.xlabel('Length of side')
plt.ylabel('Log(Volume)')
pp.savefig()
pp.close()
