#!/usr/bin/env python
"""As the basic SIR1.py, but including loss of immunity.
"""

from numpy import zeros, linspace
import matplotlib.pyplot as plt

# Time unit: 1 h
beta = 10.0 / (40 * 8 * 24)
# Reduce beta compared to SIR1.py
beta /= 4
print("beta:", beta)
gamma = 3.0 / (15 * 24)
# 6 min
dt = 0.1
# Simulate for D days
D = 300
# Corresponding no of hours
N_t = int(D * 24 / dt)
# Average loss of immunity: 50 days
nu = 1.0 / (24 * 90)

t = linspace(0, N_t * dt, N_t + 1)
S = zeros(N_t + 1)
I = zeros(N_t + 1)
R = zeros(N_t + 1)

# Initial condition
S[0] = 50
I[0] = 1
R[0] = 0

# Step equations forward in time
for n in range(N_t):
    S[n + 1] = S[n] - dt * beta * S[n] * I[n] + dt * nu * R[n]
    I[n + 1] = I[n] + dt * beta * S[n] * I[n] - dt * gamma * I[n]
    R[n + 1] = R[n] + dt * gamma * I[n] - dt * nu * R[n]

plt.plot(t, S, label="Susceptibles")
plt.plot(t, I, label="Infected")
plt.plot(t, R, label="Recovered")
plt.legend()
plt.xlabel("hours")
# plt.show()
plt.savefig("SIR2.pdf")
plt.savefig("SIR2.png")
