#!/usr/bin/env python
"""
Skylinesol.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : skylinesol
# @created     : Saturday Mar 25, 2023 19:57:33 IST
# https://iq.opengenus.org/skyline-problem/
# -*- coding: utf-8 -*-'
######################################################################
"""
from collections import namedtuple
import heapq

Building = namedtuple("Building", ["left", "right", "height"])
Edge = namedtuple("Edge", ["pos", "height"])
Strip = namedtuple("Strip", ["left", "height"])


# pylint: disable=too-few-public-methods
class SkyLine:
    """Define skyline class."""

    def getskyline(self, buildings):
        """Get skyline."""
        result = []
        edges = []

        for bldg in buildings:
            edges.append(Edge(bldg.left, -bldg.height))
            edges.append(Edge(bldg.right, bldg.height))

        edges.sort()

        heap = []
        heapq.heappush(heap, 0)
        prev = 0

        for edge in edges:
            if edge.height < 0:
                heapq.heappush(heap, edge.height)
            else:
                heap.remove(-edge.height)
                heapq.heapify(heap)
            curr = heap[0]
            if prev != curr:
                strip = Strip(edge.pos, -curr)
                result.append(strip)
                prev = curr
        return result


BLDGS = [
    Building(2, 9, 10),
    Building(3, 7, 15),
    Building(5, 12, 12),
    Building(15, 20, 10),
    Building(19, 24, 4),
]
sky = SkyLine()
strips = sky.getskyline(BLDGS)
for _ in strips:
    print(f"({_.left}, {_.height}),", end=" ")
print()
