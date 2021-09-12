#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import zeros, linspace
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('SIR1.pdf')
print("Setup Complete")

# Time unit: 1 h
beta = 10./(40*8*24)
gamma = 3./(15*24)
# 6 min
dt = 0.1            
# Simulate for D days
D = 30               
# Corresponding no of time steps
N_t = int(D*24/dt)   

t = linspace(0, N_t*dt, N_t+1)
S = zeros(N_t+1)
I = zeros(N_t+1)
R = zeros(N_t+1)

# Initial condition
S[0] = 50
I[0] = 1
R[0] = 0

# Step equations forward in time
for n in range(N_t):
    S[n+1] = S[n] - dt*beta*S[n]*I[n]
    I[n+1] = I[n] + dt*beta*S[n]*I[n] - dt*gamma*I[n]
    R[n+1] = R[n] + dt*gamma*I[n]

plt.plot(t, S, label="Susceptibles")
plt.plot(t, I, label="Infected")
plt.plot(t, R,label="Recovered")
plt.legend()
plt.xlabel('hours')
plt.ylabel('students')
plt.show()
pp.savefig()
plt.clf()

beta = 2./(40*8*24)
# Simulate for D days
D = 60  

# Corresponding no of time steps
N_t = int(D*24/dt)   

t = linspace(0, N_t*dt, N_t+1)
S = zeros(N_t+1)
I = zeros(N_t+1)
R = zeros(N_t+1)

# Initial condition
S[0] = 50
I[0] = 1
R[0] = 0

# Step equations forward in time
for n in range(N_t):
    S[n+1] = S[n] - dt*beta*S[n]*I[n]
    I[n+1] = I[n] + dt*beta*S[n]*I[n] - dt*gamma*I[n]
    R[n+1] = R[n] + dt*gamma*I[n]

plt.plot(t, S, label="Susceptibles")
plt.plot(t, I, label="Infected")
plt.plot(t, R,label="Recovered")
plt.legend()
plt.xlabel('hours')
plt.ylabel('students')
plt.show()
pp.savefig()
pp.close()
