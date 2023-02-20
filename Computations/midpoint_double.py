#!/usr/bin/env python
# -*- coding: utf-8 -*-


def midpoint(f, a, b, n):
    h = float(b - a) / n
    result = 0
    for i in range(n):
        result += f((a + h / 2.0) + i * h)
    result *= h
    return result


def midpoint_double1(f, a, b, c, d, nx, ny):
    hx = (b - a) / float(nx)
    hy = (d - c) / float(ny)
    I = 0
    for i in range(nx):
        for j in range(ny):
            xi = a + hx / 2 + i * hx
            yj = c + hy / 2 + j * hy
            I += hx * hy * f(xi, yj)
    return I


def midpoint_double2(f, a, b, c, d, nx, ny):
    def g(x):
        return midpoint(lambda y: f(x, y), c, d, ny)

    return midpoint(g, a, b, nx)
