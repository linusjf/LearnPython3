#!/usr/bin/env python
"""
Editdist.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : editdist
# @created     : Friday Mar 17, 2023 19:28:49 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""


def editdist(string1, string2):
    """Edit distance."""
    rows = len(string1)
    cols = len(string2)
    dparray = [[0] * (cols + 1) for _ in range(rows + 1)]
    for i in range(1, cols + 1):
        dparray[0][i] = i
    for i in range(1, rows + 1):
        dparray[i][0] = i
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if string1[i - 1] == string2[j - 1]:
                dparray[i][j] = dparray[i - 1][j - 1]
            else:
                dparray[i][j] = (
                    min(dparray[i - 1][j - 1], dparray[i][j - 1], dparray[i - 1][j]) + 1
                )
    return dparray[rows][cols]


# driver code
print(editdist("kitten", "sitting"))
