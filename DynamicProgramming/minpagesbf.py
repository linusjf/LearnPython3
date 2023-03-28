#!/usr/bin/env python
"""
Min pages brute force.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : minpagesbf
# @created     : Tuesday Mar 28, 2023 19:11:40 IST
# @description :
# https://www.codingninjas.com/codestudio/library/book-allocation-problem
# -*- coding: utf-8 -*-'
######################################################################
"""


def is_possible(arr, std_count, curr_min):
    """Check if possible."""
    size = len(arr)
    cnt_students = 1
    cursum = 0
    # iterate over all the books
    for i in range(size):
        # Increment student count by '1'
        if (cursum + arr[i]) > curr_min:
            cnt_students += 1
            # assign current book to next student and update curSum
            cursum = arr[i]
            # If count of students becomes greater than
            # given no. of students, return False
            if cnt_students > std_count:
                return False
        else:
            # update curSum.
            cursum += arr[i]
    return True


# function to find minimum number pages
def allocate_books(arr, students):
    """Allocate books."""
    size = len(arr)
    total = 0
    # If number student is more than number of books
    if size < students:
        return -1
    # Count total number of pages
    for i in range(size):
        total += arr[i]
    start = max(arr)
    for num_pages in range(start, total + 1):
        ans = is_possible(arr, students, num_pages)
        if ans:
            return num_pages
    return -1


# Number of pages in books
ARR = [10, 20, 30, 40]
M = 2  # No. of students
print(f"The minimum value of maximum number of pages is: {allocate_books(ARR, M)}")
