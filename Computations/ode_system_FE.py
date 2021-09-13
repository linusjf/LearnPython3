#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import linspace, zeros, asarray
import matplotlib.pyplot as plt

def ode_FE(f, U_0, dt, T):
    N_t = int(round(float(T)/dt))
    # Ensure that any list/tuple returned from f_ is wrapped as array
    f_ = lambda u, t: asarray(f(u, t))
    u = zeros((N_t+1, len(U_0)))
    t = linspace(0, N_t*dt, len(u))
    u[0] = U_0
    for n in range(N_t):
        u[n+1] = u[n] + dt*f_(u[n], t[n])
    return u, t

def demo_SIR():
    """Test case using a SIR model."""
    def f(u, t):
        S, I, R = u
        return [-beta*S*I, beta*S*I - gamma*I, gamma*I]

    beta = 10./(40*8*24)
    gamma = 3./(15*24)
    # 6 min
    dt = 0.1             
    # Simulate for D days
    D = 30               
    # Corresponding no of time steps
    N_t = int(D*24/dt)   
    # End time
    T = dt*N_t           
    U_0 = [50, 1, 0]

    u, t = ode_FE(f, U_0, dt, T)

    S = u[:,0]
    I = u[:,1]
    R = u[:,2]
    plt.plot(t, S,label="Susceptibles")
    plt.plot(t, I, label="Infected")
    plt.plot(t, R, label="Recovered")
    plt.legend()
    plt.xlabel('hours')
    plt.show()
    plt.savefig("demo_SIR.png")
    plt.savefig("demo_SIR.pdf")

    # Consistency check:
    N = S[0] + I[0] + R[0]
    eps = 1E-12  # Tolerance for comparing real numbers
    for n in range(len(S)):
        SIR_sum = S[n] + I[n] + R[n]
        if abs(SIR_sum - N) > eps:
            print('*** consistency check failed: S+I+R=%g != %g' %\
                  (SIR_sum, N))

if __name__ == '__main__':
    demo_SIR()
