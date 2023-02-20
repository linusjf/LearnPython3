#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import arange, zeros, exp, linspace
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("fe_geom.pdf")
print("Setup Complete")


def dudt(u):
    return u


def u_exact(t):
    return exp(t)


size = [4]
a = 0
b = 3
for sz in size:
    u = zeros(sz)
    u[0] = 1
    dt = 1 / (sz / 4)
    for i in arange(0, sz - 1):
        u[i + 1] = u[i] + dt * dudt(u[i])

    print(u)
    tP = arange(0, sz)
    time = linspace(a, b, 100)
    u_true = u_exact(time)
    plt.plot(time, u_true, "b-", tP, u, "ro")
    plt.xlabel("t")
    plt.ylabel("u(t)")
    pp.savefig()
    plt.clf()

pp.close()
