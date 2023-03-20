#!/usr/bin/env python
"""
Count caps.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : countcaps
# @created     : Monday Mar 20, 2023 16:15:42 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# Python program to find number of ways to wear hats
from collections import defaultdict


class AssignCap:
    """Assign caps."""

    # Initialize variables
    def __init__(self):
        """Construct object."""
        self.allmask = 0
        self.total_caps = 100
        self.caps = defaultdict(list)

    #  Mask is the set of persons, i is the current cap number.
    def count_ways_util(self, dparray, mask, cap_no):
        """Count ways util."""
        # If all persons are wearing a cap so we
        # are done and this is one way so return 1
        if mask == self.allmask:
            return 1

        # If not everyone is wearing a cap and also there are no more
        # caps left to process, so there is no way, thus return 0;
        if cap_no > self.total_caps:
            return 0

        # If we have already solved this subproblem, return the answer.
        if dparray[mask][cap_no] != -1:
            return dparray[mask][cap_no]

        # Ways, when we don't include this cap in our arrangement
        # or solution set
        ways = self.count_ways_util(dparray, mask, cap_no + 1)

        # assign ith cap one by one  to all the possible persons
        # and recur for remaining caps.
        if cap_no in self.caps:
            for ppl in self.caps[cap_no]:
                # if person 'ppl' is already wearing a cap then continue
                if mask & (1 << ppl):
                    continue
                # Else assign him this cap and recur for remaining caps with
                # new updated mask vector
                ways += self.count_ways_util(dparray, mask | (1 << ppl), cap_no + 1)
                ways = ways % (10**9 + 7)
        # Save the result and return it
        dparray[mask][cap_no] = ways
        return dparray[mask][cap_no]

    def count_ways(self, count):
        """Count ways."""
        # Reads n lines from standard input for current test case
        # create dictionary for cap. cap[i] = list of person having
        # cap no i
        for ppl in range(count):
            cap_possessed_by_person = map(int, input().strip().split())
            for i in cap_possessed_by_person:
                self.caps[i].append(ppl)

        # allmask is used to check if all persons
        # are included or not, set all n bits as 1
        self.allmask = (1 << count) - 1
        # Initialize all entries in dparray as -1
        dparray = [[-1] * (self.total_caps + 1) for _ in range(2**count)]
        # Call recursive function countWaysUtil
        # result will be in dparray[0][1]
        print(
            self.count_ways_util(
                dparray,
                0,
                1,
            )
        )


def main():
    """Execute main."""
    # number of persons in every test case
    no_of_people = int(input())
    AssignCap().count_ways(no_of_people)


if __name__ == "__main__":
    main()
