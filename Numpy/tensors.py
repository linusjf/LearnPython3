#!/usr/bin/env python
# -*- coding: utf-8 -*-
# create tensor
from numpy import array

T = array(
    [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
        [[21, 22, 23], [24, 25, 26], [27, 28, 29]],
    ]
)
print(T.shape)
print(T)

# tensor addition
# define first tensor
A = array(
    [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
        [[21, 22, 23], [24, 25, 26], [27, 28, 29]],
    ]
)
# define second tensor
B = array(
    [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
        [[21, 22, 23], [24, 25, 26], [27, 28, 29]],
    ]
)
# add tensors
C = A + B
print(C)

# tensor subtraction
# define first tensor
A = array(
    [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
        [[21, 22, 23], [24, 25, 26], [27, 28, 29]],
    ]
)
# define second tensor
B = array(
    [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
        [[21, 22, 23], [24, 25, 26], [27, 28, 29]],
    ]
)
# subtract tensors
C = A - B
print(C)

# tensor Hadamard product
# define first tensor
A = array(
    [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
        [[21, 22, 23], [24, 25, 26], [27, 28, 29]],
    ]
)
# define second tensor
B = array(
    [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
        [[21, 22, 23], [24, 25, 26], [27, 28, 29]],
    ]
)
# multiply tensors
C = A * B
print(C)

# tensor division
# define first tensor
A = array(
    [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
        [[21, 22, 23], [24, 25, 26], [27, 28, 29]],
    ]
)
# define second tensor
B = array(
    [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
        [[21, 22, 23], [24, 25, 26], [27, 28, 29]],
    ]
)
# divide tensors
C = A / B
print(C)

# tensor product
from numpy import tensordot

# define first vector
A = array([1, 2])
# define second vector
B = array([3, 4])
# calculate tensor product
C = tensordot(A, B, axes=0)
print(C)
