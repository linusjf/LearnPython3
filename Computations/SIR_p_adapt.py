#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import zeros, linspace
from matplotlib.pyplot import plot, savefig, legend, xlabel
# Time unit: 1 h
beta = 10./(40*8*24)
# reduce beta compared to SIR1.py
beta /= 4            
print('beta:', beta)
gamma = 3./(15*24)
# 6 min
dt = 0.1             
# simulate for D days
D = 200              
# corresponding no of hours
N_t = int(D*24/dt)   
# average loss of immunity
nu = 1./(24*50)      
# start point of campaign (in days)
Delta = 10           
p_0 = 0.001

t = linspace(0, N_t*dt, N_t+1)
S = zeros(N_t+1)
I = zeros(N_t+1)
R = zeros(N_t+1)
V = zeros(N_t+1)

def p(t):
    # Rely on p_0, n, S, and V as global variables
    return p_0 if (V[n] < 0.5*(S[0]+I[0]) and t > Delta*24) else 0

# Initial condition
S[0] = 50
I[0] = 1
R[0] = 0
V[0] = 0

# Step equations forward in time
for n in range(N_t):
    S[n+1] = S[n] - dt*beta*S[n]*I[n] + dt*nu*R[n] - dt*p(t[n])*S[n]
    V[n+1] = V[n] + dt*p(t[n])*S[n]
    I[n+1] = I[n] + dt*beta*S[n]*I[n] - dt*gamma*I[n]
    R[n+1] = R[n] + dt*gamma*I[n] - dt*nu*R[n]
    loss = int(V[n+1] + S[n+1] + R[n+1] + I[n+1]) - \
           int(V[0] + S[0] + R[0] + I[0])
    if loss > 0:
        print('loss: %d' % loss)

plot(t, S, t, I, t, R, t, V)
legend(['S', 'I', 'R', 'V'], loc='upper right')
xlabel('hours')
savefig('SIR_p_adapt.pdf')
savefig('SIR_p_adapt.png')
