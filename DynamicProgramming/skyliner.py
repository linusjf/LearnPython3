#!/usr/bin/env python
"""
Skyliner.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : skyliner
# @created     : Thursday Mar 23, 2023 21:17:44 IST
# https://linlaw0229.github.io/2021/06/01/218-The-Skyline-Problem/
# -*- coding: utf-8 -*-'
######################################################################
"""
from collections import namedtuple
from math import inf
import heapq

Building = namedtuple("Building", ["left", "right", "height"])
Edge = namedtuple("Edge", ["height", "right"])
Strip = namedtuple("Strip", ["left", "height"])


# pylint: disable=too-few-public-methods
class Solution:
    """Solve."""

    def get_skyline(self, buildings):
        """Get skyline."""
        print(f"buildings = {buildings}")
        events = []
        for bldg in buildings:
            events.append((bldg.left, -bldg.height, bldg.right))
            # start event, using min heap so append -H
            # need that -H in the list, not just for
            # the heap. Because, when you sort events, you
            # want to make sure for given x an event with max
            # H is processed first. ex: height 14 vs 15,
            # after negative, -15 event would come before -14 event
            events.append((bldg.right, 0, 0))
        print(f"events = {events}")
        events.sort()
        print(f"sorted events = {events}")
        res = [Strip(0, 0)]
        heap_hts = [Edge(0, inf)]
        heapmin = heap_hts[0]
        for left, neg_h, right in events:
            print(f"left = {left}, neg_h = {neg_h}, right = {right}")
            print(f"heap_hts = {heap_hts}")
            heapmin = heap_hts[0]
            # processing events
            # 1. clean out old events by pop out those right ends
            # before new event
            # 2. push the new events to the queue
            # 3. check if new largest height affect result skyline
            # pop out building which is end
            while heapmin.right <= left:
                print(f"heapmin.right <= left: {heapmin.right} {left}")
                heapq.heappop(heap_hts)
                print(f"heap_hts after pop = {heap_hts}")
                heapmin = heap_hts[0]
            # if it is a start of building, push
            # it into heap as current building
            if neg_h != 0:
                print(f"neg_h != 0: {neg_h}")
                heapq.heappush(heap_hts, Edge(neg_h, right))
                print(f"heap_hts after push = {heap_hts}")
                heapmin = heap_hts[0]
            # if change in height with previous key point, append to result
            reslast = res[-1]
            if reslast.height != -heapmin.height:
                print(f"reslast.height != -heapmin.height : {reslast.height} {-heapmin.height}")
                res.append(Strip(left, -heapmin.height))
                print(f"res = {res}")
        return res[1:]


ARR = [
    Building(1, 5, 11),
    Building(2, 7, 6),
    Building(3, 9, 13),
    Building(12, 16, 7),
    Building(14, 25, 3),
    Building(19, 22, 18),
    Building(23, 29, 13),
    Building(24, 28, 4),
]
soln = Solution().get_skyline(ARR)
for strip in soln:
    print(f"({strip.left}, {strip.height}),", end=" ")
print()
