#!/usr/bin/env python
"""
Skyline.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : skyline
# @created     : Thursday Mar 23, 2023 05:22:28 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
from collections import namedtuple

Building = namedtuple("Building", ["left", "height", "right"])
Strip = namedtuple("Strip", ["left", "height"])


class SkyLine:
    """Define class Skyline."""

    def __init__(self):
        """Construct object."""
        self.arr = []

    def count(self):
        """Return count."""
        return len(self.arr)

    def merge(self, other):
        """Merge skyline."""
        res = SkyLine()
        height1, height2, i, j = 0, 0, 0, 0
        countself = self.count()
        countother = other.count()
        while i < countself and j < countother:
            if self.arr[i].left < other.arr[j].left:
                xval1, height1 = self.arr[i].left, self.arr[i].height
                maxh = max(height1, height2)
                res.append(Strip(xval1, maxh))
                i += 1
            else:
                xval2, height2 = other.arr[j].left, other.arr[j].height
                maxh = max(height1, height2)
                res.append(Strip(xval2, maxh))
                j += 1
        while i < countself:
            res.append(self.arr[i])
            i += 1
        while j < countother:
            res.append(other.arr[j])
            j += 1
        return res

    def append(self, strip):
        """Append."""
        countself = self.count()
        if countself > 0 and self.arr[countself - 1].height == strip.height:
            return
        if countself > 0 and self.arr[countself - 1].left == strip.left:
            self.arr[countself - 1].height = max(self.arr[countself - 1].height, strip.height)
            return
        self.arr.append(strip)
        countself += 1

    def print_skyline(self):
        """Print skyline."""
        print("Skyline for given buildings is")
        for i in range(self.count()):
            print(f" ({self.arr[i].left}, {self.arr[i].height}),", end="")
        print()


def find_skyline(arr, left, right):
    """Find skyline."""
    if left == right:
        res = SkyLine()
        res.append(Strip(arr[left].left, arr[left].height))
        res.append(Strip(arr[left].right, 0))
        return res
    mid = (left + right) // 2
    skyl = find_skyline(arr, left, mid)
    skyr = find_skyline(arr, mid + 1, right)
    res = skyl.merge(skyr)
    return res


ARR = [
    Building(1, 11, 5),
    Building(2, 6, 7),
    Building(3, 13, 9),
    Building(12, 7, 16),
    Building(14, 3, 25),
    Building(19, 18, 22),
    Building(23, 13, 29),
    Building(24, 4, 28),
]
SIZE = len(ARR)
skyline = find_skyline(ARR, 0, SIZE - 1)
skyline.print_skyline()
