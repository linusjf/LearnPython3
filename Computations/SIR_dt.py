#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021  <@localhost>
#
# Distributed under terms of the MIT license.

from ode_system_FE import ode_FE
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("SIR_dt.pdf")
print("Setup Complete")


def demo_SIR():
    """Test case using an SIR model"""

    def f(u, t):
        S, I, R = u
        return [-beta * S * I, beta * S * I - gamma * I, gamma * I]

    beta = 10.0 / (40 * 8 * 24)
    gamma = 3.0 / (15 * 24)
    # 48 h
    dt = 48.0
    # Simulate for D days
    D = 30
    # Corresponding no of hours
    N_t = int(D * 24 / dt)
    # End time
    T = dt * N_t
    U_0 = [50, 1, 0]

    u_old, t_old = ode_FE(f, U_0, dt, T)
    S_old = u_old[:, 0]
    I_old = u_old[:, 1]
    R_old = u_old[:, 2]

    k = 1
    one_more = True
    while one_more == True:
        dt_k = 2 ** (-k) * dt
        u_new, t_new = ode_FE(f, U_0, dt_k, T)
        S_new = u_new[:, 0]
        I_new = u_new[:, 1]
        R_new = u_new[:, 2]

        plt.plot(
            t_old,
            S_old,
            "b-",
            t_new,
            S_new,
            "b--",
            t_old,
            I_old,
            "r-",
            t_new,
            I_new,
            "r--",
            t_old,
            R_old,
            "g-",
            t_new,
            R_new,
            "g--",
        )
        plt.xlabel("hours")
        plt.ylabel("S (blue), I (red), R (green)")
        # plt.savefig("SIR_dt_" + str(dt_k) + ".png")
        plt.title("dt = " + str(dt_k))
        pp.savefig()
        plt.clf()

        print("Finest timestep was: ", dt_k)
        answer = input("Do one more with finer dt (y/n)? ")
        if answer == "y":
            S_old = S_new.copy()
            R_old = R_new.copy()
            I_old = I_new.copy()
            t_old = t_new.copy()
            k += 1
        else:
            one_more = False


if __name__ == "__main__":
    demo_SIR()
    pp.close()
