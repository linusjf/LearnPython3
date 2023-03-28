#!/usr/bin/env python
"""
Min pages.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : minpages
# @created     : Tuesday Mar 28, 2023 10:13:44 IST
# @description : Python3 program for optimal allocation of pages
# https://www.geeksforgeeks.org/allocate-minimum-number-pages/
# -*- coding: utf-8 -*-'
######################################################################
"""
from math import inf


# Utility function to check if
# current minimum value is feasible or not.
def is_possible(arr, student_count, curr_min):
    """Check if possible."""
    size = len(arr)
    students_required = 1
    curr_sum = 0
    if max(arr) > curr_min:
        return False
    # iterate over all books
    for i in range(size):
        if (curr_sum + arr[i]) > curr_min:
            students_required += 1
            # update curr_sum
            curr_sum = arr[i]
            # if students required becomes greater
            # than given no. of students, return False
            if students_required > student_count:
                return False
        else:
            curr_sum += arr[i]
    return True


# function to find minimum pages
def find_pages(arr, student_count):
    """Find pages."""
    size = len(arr)
    total = 0
    # return -1 if no. of books is
    # less than no. of students
    if size < student_count:
        return -1
    # Count total number of pages
    for i in range(size):
        total += arr[i]
    print(f"Total = {total}")
    # initialize start as 0 pages and
    # end as total pages
    start, end = max(arr), total
    result = inf
    # traverse until start <= end
    print("Start | End  | Mid | Possible")
    while start <= end:
        # check if it is possible to distribute
        # books by using mid as current minimum
        mid = (start + end) // 2
        poss = is_possible(arr, student_count, mid)
        print(f"{start} | {end}  | {mid} | {poss}")
        if poss:
            # update result to current distribution
            # as it's the best we have found till now.
            result = mid
            # as we are finding minimum and books
            # are sorted so reduce end = mid -1
            # that means
            end = mid - 1
        else:
            # if not possible means pages should be
            # increased so update start = mid + 1
            start = mid + 1
    # at-last return minimum no. of pages
    return result


# Driver Code
# Number of pages in books
ARR = [12, 34, 67, 90]
print(f"ARR = {ARR}")
M = 2  # No. of students
print(f"No. of students = {M}")
print(f"Minimum number of pages = {find_pages(ARR, M)}")
ARR = [10, 20, 30, 40]
print(f"ARR = {ARR}")
M = 2  # No. of students
print(f"No. of students = {M}")
print(f"Minimum number of pages = {find_pages(ARR, M)}")
