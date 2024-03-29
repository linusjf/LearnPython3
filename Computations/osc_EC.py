#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("osc_EC.pdf")
print("Setup Complete")

omega = 2
P = 2 * np.pi / omega
dts = (P / 20, P / 40, P / 160, P / 2000)
T = 40 * P
T = P
for dt in dts:
    N_t = int(round(T / dt))
    t = np.linspace(0, N_t * dt, N_t + 1)
    print("N_t:", N_t)

    u = np.zeros(N_t + 1)
    v = np.zeros(N_t + 1)

    # Initial condition
    X_0 = 2
    u[0] = X_0
    v[0] = 0

    # Step equations forward in time
    for n in range(N_t):
        v[n + 1] = v[n] - dt * omega**2 * u[n]
        u[n + 1] = u[n] + dt * v[n + 1]

    # Plot the last four periods to illustrate the accuracy
    # in long time simulations
    N4l = int(round(4 * P / dt))  # No of intervals to be plotted
    l1, l2 = plt.plot(t[-N4l:], u[-N4l:], "b-", t[-N4l:], X_0 * np.cos(omega * t)[-N4l:], "r--")
    plt.legend((l1, l2), ("numerical", "exact"), loc="upper left")
    plt.xlabel("t")
    plt.title("dt = " + str(dt))
    pp.savefig()
    plt.clf()
    print("{:.16f} {:.16f}".format(u[-1], v[-1]))

pp.close()
