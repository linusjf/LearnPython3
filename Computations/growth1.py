#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import linspace, zeros, exp
import matplotlib.pyplot as plt

N_0 = int(input("Give initial population size N_0: "))
r = float(input("Give net growth rate r: "))
dt = float(input("Give time step size: "))
N_t = int(input("Give number of steps: "))
t = linspace(0, N_t * dt, N_t + 1)
N = zeros(N_t + 1)

N[0] = N_0
for n in range(N_t):
    N[n + 1] = N[n] + r * dt * N[n]

numerical_sol = "bo" if N_t < 70 else "b-"
plt.plot(t, N, numerical_sol, t, N_0 * exp(r * t), "r-")
plt.legend(["numerical", "exact"], loc="upper left")
plt.xlabel("t")
plt.ylabel("N(t)")
filestem = "growth1_%dsteps" % N_t
plt.savefig("%s.png" % filestem)
plt.savefig("%s.pdf" % filestem)
