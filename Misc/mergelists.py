#!/usr/bin/env python
# -*- coding: utf-8 -*-

import heapq


def merge(lists):
    print("Input lists: ", end="")
    print(lists)
    merged_list = []

    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)
    print("Heap = ", end="")
    print(heap)

    while heap:
        val, list_ind, element_ind = heapq.heappop(heap)

        print("Appending ... ", end="")
        print(val)
        merged_list.append(val)

        if element_ind + 1 < len(lists[list_ind]):
            next_tuple = (lists[list_ind][element_ind + 1], list_ind, element_ind + 1)
            heapq.heappush(heap, next_tuple)
            print("Added next tuple", end="")
            print(next_tuple)
            print("New Heap = ", end="")
            print(heap)
    print("Merged list = ", end="")
    return merged_list


lists = []
print(merge(lists))
print("")

lists = [[], [], []]
print(merge(lists))
print("")

lists = [[], [1], [1, 2]]
print(merge(lists))
print("")

lists = [[1]]
print(merge(lists))
print("")

lists = [[1], [1, 3, 5], [1, 10, 20, 30, 40]]
print(merge(lists))
print("")
