#!/usr/bin/env python
"""
Uglynos.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : uglynos
# @created     : Tuesday Mar 21, 2023 11:09:48 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# Python program to find n'th Ugly number
# Function to get the nth ugly number


def get_nth_uglyno(num):
    """Get nth ugly number."""
    ugly = [0] * num  # To store ugly numbers
    # 1 is the first ugly number
    ugly[0] = 1
    # i2, i3, i5 will indicate indices for
    # 2,3,5 respectively
    i2 = i3 = i5 = 0  # pylint: disable=invalid-name
    # Set initial multiple value
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5
    # Start loop to find value from
    # ugly[1] to ugly[n]
    for idx in range(1, num):
        # Choose the min value of all
        # available multiples
        ugly[idx] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
        # Increment the value of index accordingly
        if ugly[idx] == next_multiple_of_2:
            i2 += 1  # pylint: disable=invalid-name
            next_multiple_of_2 = ugly[i2] * 2
        if ugly[idx] == next_multiple_of_3:
            i3 += 1  # pylint: disable=invalid-name
            next_multiple_of_3 = ugly[i3] * 3
        if ugly[idx] == next_multiple_of_5:
            i5 += 1  # pylint: disable=invalid-name
            next_multiple_of_5 = ugly[i5] * 5
    # Return ugly[n] value
    return ugly[-1]


# Driver Code
def main():
    """Run main."""
    print(get_nth_uglyno(150))


if __name__ == "__main__":
    main()
