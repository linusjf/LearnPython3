#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import zeros, linspace
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("SIR_Heun.pdf")
print("Setup Complete")

# Time unit: 1 h
beta = 10.0 / (40 * 8 * 24)
gamma = 3.0 / (15 * 24)
# Large and smalls dts
dts = (24.0, 4.0)
# Simulate for D days
D = 30
for dt in dts:
    # Corresponding no of hours
    N_t = int(D * 24 / dt)

    t = linspace(0, N_t * dt, N_t + 1)
    S_FE = zeros(N_t + 1)
    I_FE = zeros(N_t + 1)
    R_FE = zeros(N_t + 1)
    S_H = zeros(N_t + 1)
    I_H = zeros(N_t + 1)
    R_H = zeros(N_t + 1)

    # Initial condition
    S_FE[0] = 50
    I_FE[0] = 1
    R_FE[0] = 0
    S_H[0] = 50
    I_H[0] = 1
    R_H[0] = 0

    # Step equations forward in time
    for n in range(N_t):
        # FE
        S_FE[n + 1] = S_FE[n] - dt * beta * S_FE[n] * I_FE[n]
        I_FE[n + 1] = I_FE[n] + dt * beta * S_FE[n] * I_FE[n] - dt * gamma * I_FE[n]
        R_FE[n + 1] = R_FE[n] + dt * gamma * I_FE[n]
        # H  (predict and then update)
        S_p = S_H[n] - dt * beta * S_H[n] * I_H[n]
        I_p = I_H[n] + dt * beta * S_H[n] * I_H[n] - dt * gamma * I_H[n]
        R_p = R_H[n] + dt * gamma * I_H[n]

        S_H[n + 1] = S_H[n] - (dt / 2.0) * (beta * S_H[n] * I_H[n] + beta * S_p * I_p)
        I_H[n + 1] = I_H[n] + (dt / 2.0) * (
            beta * S_H[n] * I_H[n] - gamma * I_H[n] + beta * S_p * I_p - gamma * I_p
        )
        R_H[n + 1] = R_H[n] + (dt / 2.0) * (gamma * I_H[n] + gamma * I_p)

    # fig = plt.figure()
    l1, l2, l3, l4, l5, l6 = plt.plot(t, S_FE, t, I_FE, t, R_FE, t, S_H, t, I_H, t, R_H)
    plt.legend((l1, l2, l3, l4, l5, l6), ("S (FE)", "I (FE)", "R (FE)", "S (H)", "I (H)", "R (H)"))
    plt.xlabel("hours")
    plt.title("dt = " + str(dt))
    pp.savefig()
    plt.clf()

pp.close()
