#!/usr/bin/env python
from numpy import zeros, linspace, pi, cos, array
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("osc_FE.pdf")
print("Setup Complete")

omega = 2
P = 2 * pi / omega
dts = (P / 20, P / 40, P / 160, P / 2000)
T = 3 * P
for dt in dts:
    N_t = int(round(T / dt))
    t = linspace(0, N_t * dt, N_t + 1)

    u = zeros(N_t + 1)
    v = zeros(N_t + 1)

    # Initial condition
    X_0 = 2
    u[0] = X_0
    v[0] = 0

    # Step equations forward in time
    for n in range(N_t):
        u[n + 1] = u[n] + dt * v[n]
        v[n + 1] = v[n] - dt * omega**2 * u[n]

    l1, l2 = plt.plot(t, u, "b-", t, X_0 * cos(omega * t), "r--")
    plt.legend((l1, l2), ("numerical", "exact"), loc="upper left")
    plt.xlabel("t")
    plt.title("dt = " + str(dt))
    pp.savefig()
    plt.clf()

pp.close()
