#!/usr/bin/env python
# -*- coding: utf-8 -*-


def midpoint_triple1(g, a, b, c, d, e, f, nx, ny, nz):
    hx = (b - a) / float(nx)
    hy = (d - c) / float(ny)
    hz = (f - e) / float(nz)
    I = 0
    for i in range(nx):
        for j in range(ny):
            for k in range(nz):
                xi = a + hx / 2 + i * hx
                yj = c + hy / 2 + j * hy
                zk = e + hz / 2 + k * hz
                I += hx * hy * hz * g(xi, yj, zk)
    return I


def midpoint(f, a, b, n):
    h = float(b - a) / n
    result = 0
    for i in range(n):
        result += f((a + h / 2.0) + i * h)
    result *= h
    return result


def midpoint_triple2(g, a, b, c, d, e, f, nx, ny, nz):
    def p(x, y):
        return midpoint(lambda z: g(x, y, z), e, f, nz)

    def q(x):
        return midpoint(lambda y: p(x, y), c, d, ny)

    return midpoint(q, a, b, nx)
