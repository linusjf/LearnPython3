#!/usr/bin/env python
"""
Gramschmidt.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : gramschmidt
# @created     : Thursday Oct 12, 2023 10:32:53 IST
# @description : https://tiny.cc/9l7cvz
# https://gist.github.com/iizukak/1287876/edad3c337844fac34f7e56ec09f9cb27d4907cc7
# -*- coding: utf-8 -*-'
######################################################################
"""
import numpy as np


def gs_coefficient(vone, vtwo):
    """ calculate gs coefficient """
    return np.dot(vone, vtwo) / np.dot(vone, vone)


def multiply(coefficient, vec):
    """ multiply vector with coefficient """
    return list(map((lambda x: x * coefficient), vec))


def proj(vone, vtwo):
    """ calculate projection """
    return multiply(gs_coefficient(vone, vtwo), vone)


def gram_schmidt(xvec):
    """ Calculate gram schmidt orthogonalization vector """
    yvec = []
    for _, elem in enumerate(xvec):
        temp_vec = elem
        for in_y in yvec:
            proj_vec = proj(in_y, elem)
            #  print("i =", _, ", projection vector =", proj_vec)
            temp_vec = list(map(lambda x, y: x - y, temp_vec, proj_vec))
            #  print("i =", _, ", temporary vector =", temp_vec)
        yvec.append(temp_vec)
    return yvec


def basis(yvec):
    """ Calculate gram schmidt basis """
    length = len(yvec)
    qvec = np.zeros((length, length))
    for _, elem in enumerate(yvec):
        temp_vec = elem / np.sqrt(np.dot(elem, elem))
        qvec[_] = temp_vec
    return qvec


test = np.array([[3.0, 1.0], [2.0, 2.0]])
test2 = np.array([[1.0, 1.0, 0.0], [1.0, 3.0, 1.0], [2.0, -1.0, 1.0]])
A = np.array([[1.0, 1.0, 1.0], [1.0, 2.0, 2.0], [1.0, 1.0, 0.0]])

print("Gram Schmidt orthogonalization result")
print(gram_schmidt(test))
print("Gram Schmidt orthogonalization basis")
print(basis(gram_schmidt(test)))
print("Gram Schmidt orthogonalization result")
print(gram_schmidt(test2))
print("Gram Schmidt orthogonalization basis")
print(basis(gram_schmidt(test2)))
print("Gram Schmidt orthogonalization result")
print(gram_schmidt(A))
print("Gram Schmidt orthogonalization basis")
print(basis(gram_schmidt(A)))
