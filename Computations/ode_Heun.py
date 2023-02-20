from numpy import linspace, zeros, exp


def ode_Heun(f, U_0, dt, T):
    N_t = int(round(float(T) / dt))
    u = zeros(N_t + 1)
    t = linspace(0, N_t * dt, len(u))
    u[0] = U_0
    for n in range(N_t):
        u_star = u[n] + dt * f(u[n], t[n])
        u[n + 1] = u[n] + 0.5 * dt * (f(u[n], t[n]) + f(u_star, t[n]))
    return u, t
