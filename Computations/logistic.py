#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ode_FE import ode_FE
import matplotlib.pyplot as plt

for dt, T in zip((0.5, 20), (60, 100)):
    u, t = ode_FE(f=lambda u, t: 0.1 * (1 - u / 500.0) * u, U_0=100, dt=dt, T=T)
    # Make separate figures for each pass in the loop
    plt.figure()
    plt.plot(t, u, "b-")
    plt.xlabel("t")
    plt.ylabel("N(t)")
    plt.savefig("tmp_%g.png" % dt)
    plt.savefig("tmp_%g.pdf" % dt)
