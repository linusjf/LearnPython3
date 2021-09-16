#!/usr/bin/env python

from numpy import linspace, zeros, exp
from ode_FE import ode_FE
from ode_Heun import ode_Heun
from matplotlib import pyplot as plt

def demo_ode_Heun():
    """Test case: u' = u, u(0) = 1"""
    def f(u,t):
        return u

    u_Heun, t = ode_Heun(f=f, U_0=1, dt=0.5, T=6)
    u_FE, t   = ode_FE(f=f, U_0=1, dt=0.5, T=6)
    l1, l2, l3 = plt.plot(t, u_Heun,'b-', t, u_FE,'b--', t, exp(t),'r--')
    plt.legend((l1, l2, l3), ('Heun', 'Forward Euler', 'True value'),loc = 'upper left')
    plt.xlabel('t')
    plt.savefig("demo_ode_Heun.pdf")
    plt.savefig("demo_ode_Heun.png")

if __name__ == '__main__':
    demo_ode_Heun()
