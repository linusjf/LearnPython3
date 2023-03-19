#!/usr/bin/env python
"""
Hungarian.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : hungarian
# @created     : Saturday Mar 18, 2023 16:20:07 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import numpy as np


# zero_mat = boolean matrix, mark_zero = blank list
def min_zero_row(zero_mat, mark_zero):
    """Find min zero row."""
    # Find the row
    min_row = [99999, -1]

    for row_num in range(zero_mat.shape[0]):
        print(f"row_num = {row_num}")
        rowsum = np.sum(zero_mat[row_num])
        print(f"rowsum = {rowsum}")
        if rowsum and min_row[0] > rowsum:
            min_row = [rowsum, row_num]

    print(min_row)
    # Marked the specific row and column as False
    zero_index = np.where(zero_mat[min_row[1]])[0][0]
    print(zero_index)
    mark_zero.append((min_row[1], zero_index))
    zero_mat[min_row[1], :] = False
    zero_mat[:, zero_index] = False


def hungarian_algorithm(mat):
    """Solve with hungarian algorithm."""
    dim = mat.shape
    curr_mat = mat
    # Step 1 - Every column and every row subtract its internal minimum
    for row_num in range(dim[0]):
        curr_mat[row_num] = curr_mat[row_num] - np.min(curr_mat[row_num])
    for col_num in range(dim[1]):
        curr_mat[:, col_num] = curr_mat[:, col_num] - np.min(curr_mat[:, col_num])

    print(curr_mat)
    zero_bool_mat = curr_mat == 0
    print(zero_bool_mat)
    zero_bool_mat_copy = zero_bool_mat.copy()

    marked_zero = []
    while True in zero_bool_mat_copy:
        min_zero_row(zero_bool_mat_copy, marked_zero)

    print(zero_bool_mat_copy)
    print(marked_zero)
    return 0


def main():
    """Run the main program."""
    # profit_matrix = np.random.randint(10, size=(5, 5))
    # Using the maximum value of the profit_matrix to get the corresponding cost_matrix
    # max_value = np.max(profit_matrix)
    # Using the cost matrix to find which positions are the answer
    # cost_matrix = max_value - profit_matrix
    # print(f"The profit matrix is:\n{profit_matrix}", f"\nThe cost matrix is:\n{cost_matrix}")
    # ans_pos = hungarian_algorithm(cost_matrix.copy())
    # print(ans_pos)

    cost_matrix = np.array(
        [[7, 6, 2, 9, 2], [6, 2, 1, 3, 9], [5, 6, 8, 9, 5], [6, 8, 5, 8, 6], [9, 5, 6, 4, 7]]
    )
    print(f"\nThe cost matrix is:\n{cost_matrix}")
    ans_pos = hungarian_algorithm(cost_matrix.copy())
    print(ans_pos)
    return 0


if __name__ == "__main__":
    main()
