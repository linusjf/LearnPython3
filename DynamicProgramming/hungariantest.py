#!/usr/bin/env python
"""
Hungarian Test.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : hungariantest
# @created     : Sunday Mar 19, 2023 20:58:47 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import numpy as np
from hungarian import hungarian_algorithm  # type: ignore
from hungarian import ans_calculation  # type: ignore


def main():
    """Run main."""
    # Hungarian Algorithm:
    # Finding the minimum value in linear assignment problem.
    # Therefore, we can find the minimum value set in net matrix
    # by using Hungarian Algorithm. In other words, the maximum value
    # and elements set in cost matrix are available."""

    # The matrix who you want to find the minimum sum
    cost_matrix = np.array(
        [[7, 6, 2, 9, 2], [6, 2, 1, 3, 9], [5, 6, 8, 9, 5], [6, 8, 5, 8, 6], [9, 5, 6, 4, 7]]
    )
    ans_pos = hungarian_algorithm(cost_matrix.copy())  # Get the element position.
    # Get the minimum or maximum value and corresponding matrix.
    ans, ans_mat = ans_calculation(cost_matrix, ans_pos)
    # Show the result
    print(f"Linear Assignment problem result: {ans:.0f}\n{ans_mat}")

    # If you want to find the maximum value, using the code as follows:
    # Using maximum value in the cost_matrix and cost_matrix to get net_matrix
    profit_matrix = np.array(
        [[7, 6, 2, 9, 2], [6, 2, 1, 3, 9], [5, 6, 8, 9, 5], [6, 8, 5, 8, 6], [9, 5, 6, 4, 7]]
    )
    max_value = np.max(profit_matrix)
    cost_matrix = max_value - profit_matrix
    ans_pos = hungarian_algorithm(cost_matrix.copy())  # Get the element position.
    ans, ans_mat = ans_calculation(profit_matrix, ans_pos)
    # Get the minimum or maximum value and corresponding matrix.
    # Show the result
    print(f"Linear Assignment problem result: {ans:.0f}\n{ans_mat}")

    cost_matrix = np.array([[8, 4, 7, 0], [5, 2, 3, 0], [9, 6, 7, 0], [9, 4, 8, 0]])
    ans_pos = hungarian_algorithm(cost_matrix.copy())  # Get the element position.
    # Get the minimum or maximum value and corresponding matrix.
    ans, ans_mat = ans_calculation(cost_matrix, ans_pos)
    # Show the result
    print(f"Linear Assignment problem result: {ans:.0f}\n{ans_mat}")


if __name__ == "__main__":
    main()
