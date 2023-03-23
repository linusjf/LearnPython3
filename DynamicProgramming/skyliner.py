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
        res = [(0, 0)]
        heap = [Edge(0, inf)]
        for left, neg_h, right in events:
            print(f"left = {left}, neg_h = {neg_h}, right = {right}")
            print(f"heap = {heap}")
            # processing events
            # 1. clean out old events by pop out those right ends
            # before new event
            # 2. push the new events to the queue
            # 3. check if new largest height affect result skyline
            # pop out building which is end
            while heap[0].right <= left:
                heapq.heappop(heap)
            print(f"heap after pop = {heap}")
            # if it is a start of building, push
            # it into heap as current building
            if neg_h != 0:
                heapq.heappush(heap, Edge(neg_h, right))
            print(f"heap after push = {heap}")
            # if change in height with previous key point, append to result
            if res[-1][1] != -heap[0].height:
                res.append((left, -heap[0].height))
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
print(Solution().get_skyline(ARR))
