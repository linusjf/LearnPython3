#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import linspace, zeros, exp
import matplotlib.pyplot as plt

def ode_FE(f, U_0, dt, T):
    N_t = int(round(float(T)/dt))
    u = zeros(N_t+1)
    t = linspace(0, N_t*dt, len(u))
    u[0] = U_0
    for n in range(N_t):
        u[n+1] = u[n] + dt*f(u[n], t[n])
    return u, t

def demo_population_growth():
    """Test case: u'=r*u, u(0)=100."""
    def f(u, t):
        return 0.1*u

    u, t = ode_FE(f=f, U_0=100, dt=0.5, T=20)
    plt.plot(t, u, label="ode")
    plt.plot(t, 100*exp(0.1*t), label="actual")
    plt.xlabel("time (t)")
    plt.ylabel("popn (u)")
    plt.legend()
    plt.show()
    plt.savefig("ode_FE.pdf")

if __name__ == '__main__':
    demo_population_growth()
