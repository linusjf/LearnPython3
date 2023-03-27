#!/usr/bin/env python
"""
Skylinebf.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : skylinebf
# @created     : Monday Mar 27, 2023 14:31:44 IST
# https://www.codingninjas.com/codestudio/library/the-skyline-problem
# -*- coding: utf-8 -*-'
######################################################################
"""


def getskyline(buildings):
    """Get skyline using brute force."""
    keys = []
    for building in buildings:
        keys.append(building[0])
        keys.append(building[1])
    keys.sort()
    last = 0
    lastkey = -1
    result = []
    for left in keys:
        if left == lastkey:
            continue
        lastkey = left
        height = 0
        for building in buildings:
            if left in range(building[0], building[1]):
                height = max(height, building[2])
            elif building[0] > left:
                break
        if height != last:
            temp = []
            temp.insert(0, left)
            temp.append(height)
            result.append(temp)
        last = height
    return result


def main():
    """Execute main."""
    buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    ans = getskyline(buildings)
    for _, elem in enumerate(ans):
        print(f"({elem[0]} {elem[1]}), ", end=" ")
    print()


if __name__ == "__main__":
    main()
