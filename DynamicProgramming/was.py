#!/usr/bin/env python
"""
Was.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : was
# @created     : Monday Mar 13, 2023 09:33:35 IST
# @description : Weighted Activity Scheduling.
# -*- coding: utf-8 -*-'
######################################################################
"""
# Python3 program for weighted job scheduling using
from collections import namedtuple

# Importing the following module to sort array
# based on our custom comparison function
from functools import cmp_to_key
from functools import lru_cache
from timeit import timeit

Job = namedtuple("Job", ["start", "finish", "profit"])


# A utility function that is used for
# sorting events according to finish time
def job_comparator(event1, event2):
    """Sort events according to finish time."""
    return event1.finish < event2.finish


# Find the latest job (in sorted array) that
# doesn't conflict with the job[i]. If there
# is no compatible job, then it returns -1
def latest_non_conflict(arr, index):
    """Find latest non conflicting job."""
    for j in range(index - 1, -1, -1):
        if arr[j].finish <= arr[index - 1].start:
            return j
    return -1


# A recursive function that returns the
# maximum possible profit from given
# array of jobs. The array of jobs must
# be sorted according to finish time
@lru_cache
def find_max_profit_rec(arr, index):
    """Find max profit recursively."""
    # Base case
    if index == 1:
        return arr[index - 1].profit

    # Find profit when current job is included
    incl_prof = arr[index - 1].profit
    i = latest_non_conflict(arr, index)
    if i != -1:
        incl_prof += find_max_profit_rec(arr, i + 1)
    # Find profit when current job is excluded

    excl_prof = find_max_profit_rec(arr, index - 1)
    return max(incl_prof, excl_prof)


# Naive Recursive Method
# The main function that returns the maximum
# possible profit from given array of jobs
def find_max_profit(arr, count):
    """Find maximum profit."""
    # Sort jobs according to finish time
    sorted_arr = sorted(arr, key=cmp_to_key(job_comparator))
    return find_max_profit_rec(tuple(sorted_arr), count)


def find_max_profit_dp(arr, count):
    """Find max profit dynamically."""
    sorted_arr = sorted(arr, key=cmp_to_key(job_comparator))
    table = [None] * count
    table[0] = sorted_arr[0].profit
    # Fill entries in M[] using recursive property
    for i in range(1, count):
        # Find profit including the current job
        incl_prof = sorted_arr[i].profit
        latest = latest_non_conflict(sorted_arr, i)
        if latest != -1:
            incl_prof += table[latest]
        # Store maximum of including and excluding
        table[i] = max(incl_prof, table[i - 1])
    return table[count - 1]


# Driver code
values = [(3, 10, 20), (1, 2, 50), (6, 19, 100), (2, 100, 200)]

jobs = []

for job in values:
    jobs.append(Job(job[0], job[1], job[2]))

NUM_JOBS = len(jobs)
print("The optimal profit (recursively) is", find_max_profit(jobs, NUM_JOBS))
print("The optimal profit (dynamically) is", find_max_profit_dp(jobs, NUM_JOBS))
print(timeit("find_max_profit(jobs, NUM_JOBS)", number=1, globals=globals()))
print(timeit("find_max_profit_dp(jobs, NUM_JOBS)", number=1, globals=globals()))
