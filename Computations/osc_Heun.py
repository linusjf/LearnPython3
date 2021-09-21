#!/usr/bin/env python
from numpy import zeros, linspace, pi, cos
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('osc_Heun.pdf')
print("Setup Complete")

def osc_Heun(X_0, omega, dt, T):
    N_t = int(round(T/dt))
    u = zeros(N_t+1)
    v = zeros(N_t+1)
    t = linspace(0, N_t*dt, N_t+1)

    # Initial condition
    u[0] = X_0
    v[0] = 0

    # Step equations forward in time
    for n in range(N_t):
        u_star = u[n] + dt*v[n]
        v_star = v[n] - dt*omega**2*u[n]
        u[n+1] = u[n] + 0.5*dt*(v[n] + v_star)
        v[n+1] = v[n] - 0.5*dt*omega**2*(u[n] + u_star)
    return u, v, t

def demo():
    omega = 2
    P = 2*pi/omega
    dts = (P/20,P/40,P/160,P/2000)
    T = 10*P
    X_0 = 2
    for dt in dts:
        u, v, t = osc_Heun(X_0, omega, dt, T)

        l1, l2 = plt.plot(t, u, 'b-', t, X_0*cos(omega*t), 'r--')
        plt.legend((l1, l2), ('numerical', 'exact'), loc='upper left')
        plt.xlabel('t')
        plt.title(f"dt = {dt:.5f}")
        pp.savefig()
        plt.clf()

if __name__ == '__main__':
    demo()
    pp.close()
