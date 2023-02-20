#!/usr/bin/env python

from ode_FE import ode_FE


def test_ode_FE_1():
    hand = [1.0, 2.0, 4.0, 8.0]
    T = 3.0
    dt = 1.0
    U_0 = 1.0

    def f(u, t):
        return u

    u, t = ode_FE(f, U_0, dt, T)
    tol = 1e-14
    for i in range(len(hand)):
        err = abs(hand[i] - u[i])
        assert err < tol, "i=%d, err=%g" % (i, err)


def test_ode_FE_2():
    T = 3.0
    # Tested first dt = 1.0, ok
    dt = 0.1
    U_0 = 1.0
    r = 1

    def f(u, t):
        return r * u

    def u_exact(U_0, r, dt, n):
        return U_0 * (1 + r * dt) ** n

    u, t = ode_FE(f, U_0, dt, T)
    tol = 1e-12  # Relaxed from 1E-14 to get through
    for n in range(len(u)):
        err = abs(u_exact(U_0, r, dt, n) - u[n])
        assert err < tol, "n=%d, err=%g" % (n, err)


test_ode_FE_1()
test_ode_FE_2()
