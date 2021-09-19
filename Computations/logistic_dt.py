#!/usr/bin/env python

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : logistic_dt
# @created     : Monday Sep 20, 2021 05:00:05 IST
# @description : 
# -*- coding: utf-8 -*-'
######################################################################

from ode_FE import ode_FE
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('logistic_dt.pdf')
print("Setup Complete")

dt = 20; T = 100
u_old, t_old = ode_FE(f=lambda u, t: 0.1*(1-u/500.)*u,
                      U_0=100, dt=dt, T=T)
k = 1
one_more = True
while one_more == True:
    dt_k = 2**(-k)*dt
    u_new, t_new = ode_FE(f=lambda u, t: 0.1*(1-u/500.)*u,
                  U_0=100, dt=dt_k, T=T)
    plt.plot(t_old,u_old,'b-',t_new,u_new,'r--')
    plt.xlabel('t'); plt.ylabel('N(t)');
    pp.savefig()
    plt.clf()
    print("Timestep was: ", dt_k)
    answer = input('Do one more with finer dt (y/n)? ')
    if answer == 'y':
        u_old = u_new.copy()
        t_old = t_new.copy()
    else:
        one_more = False
    k += 1
pp.close()
