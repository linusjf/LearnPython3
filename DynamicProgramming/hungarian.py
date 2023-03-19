#!/usr/bin/env python
"""
Hungarian.

# @file        : hungarian
# @created     : Saturday Mar 18, 2023 16:20:07 IST
# @description :
# -*- coding: utf-8 -*-"
######################################################################
"""
import numpy as np


def min_zero_row(zero_mat, mark_zero):
    """Compute min zero row."""
    # The function can be splitted into two steps:
    # 1 The function is used to find the row which containing the fewest 0.
    # 2 Select the zero number on the row, and then marked the element
    # corresponding row and column as False

    # Find the row
    min_row = [99999, -1]

    for row_num in range(zero_mat.shape[0]):
        row_sum = np.sum(zero_mat[row_num])
        if row_sum and min_row[0] > row_sum:
            min_row = [row_sum, row_num]

    # Marked the specific row and column as False
    zero_index = np.where(zero_mat[min_row[1]])[0][0]
    mark_zero.append((min_row[1], zero_index))
    zero_mat[min_row[1], :] = False
    zero_mat[:, zero_index] = False


def mark_matrix(mat):  # noqa
    """Find the returning possible solutions for LAP problem."""

    # Transform the matrix to boolean matrix(0 = True, others = False)
    cur_mat = mat
    zero_bool_mat = cur_mat == 0
    zero_bool_mat_copy = zero_bool_mat.copy()

    # Recording possible answer positions by marked_zero
    marked_zero = []
    while True in zero_bool_mat_copy:
        min_zero_row(zero_bool_mat_copy, marked_zero)

    # Recording the row and column positions seperately.
    marked_zero_row = []
    marked_zero_col = []
    for _, row in enumerate(marked_zero):
        marked_zero_row.append(row[0])
        marked_zero_col.append(row[1])

    # Step 2-2-1
    non_marked_row = list(set(range(cur_mat.shape[0])) - set(marked_zero_row))
    marked_cols = []
    check_switch = True
    while check_switch:
        check_switch = False
        for _, row in enumerate(non_marked_row):
            row_array = zero_bool_mat[row, :]
            for j in range(row_array.shape[0]):
                # Step 2-2-2
                if row_array[j] and j not in marked_cols:
                    # Step 2-2-3
                    marked_cols.append(j)
                    check_switch = True

        for row_num, col_num in marked_zero:
            # Step 2-2-4
            if row_num not in non_marked_row and col_num in marked_cols:
                # Step 2-2-5
                non_marked_row.append(row_num)
                check_switch = True
    # Step 2-2-6
    marked_rows = list(set(range(mat.shape[0])) - set(non_marked_row))

    return marked_zero, marked_rows, marked_cols


def adjust_matrix(mat, cover_rows, cover_cols):  # noqa
    """Adjust matrix."""
    cur_mat = mat
    non_zero_element = []

    # Step 4-1
    for row_idx, row in enumerate(cur_mat):
        if row_idx not in cover_rows:
            for i, elem in enumerate(row):
                if i not in cover_cols:
                    non_zero_element.append(elem)
    min_num = min(non_zero_element)

    # Step 4-2
    for row, rowdata in enumerate(cur_mat):
        if row not in cover_rows:
            for i, elem in enumerate(rowdata):
                if i not in cover_cols:
                    cur_mat[row, i] = elem - min_num
    # Step 4-3
    for row, rowdata in enumerate(cover_rows):
        for col, elem in enumerate(cover_cols):
            cur_mat[cover_rows[row], cover_cols[col]] = (
                cur_mat[cover_rows[row], cover_cols[col]] + min_num
            )
    return cur_mat


def hungarian_algorithm(mat):
    """Solve Hungarian algorithm."""
    dim = mat.shape[0]
    cur_mat = mat
    ans_pos = -1
    # Step 1 - Every column and every row subtract its internal minimum
    for row_num in range(mat.shape[0]):
        cur_mat[row_num] = cur_mat[row_num] - np.min(cur_mat[row_num])
    for col_num in range(mat.shape[1]):
        cur_mat[:, col_num] = cur_mat[:, col_num] - np.min(cur_mat[:, col_num])
    zero_count = 0
    while zero_count < dim:
        # Step 2 & 3
        ans_pos, marked_rows, marked_cols = mark_matrix(cur_mat)
        zero_count = len(marked_rows) + len(marked_cols)

        if zero_count < dim:
            cur_mat = adjust_matrix(cur_mat, marked_rows, marked_cols)

    return ans_pos


def ans_calculation(mat, pos):
    """Calculate answer."""
    total = 0
    ans_mat = np.zeros((mat.shape[0], mat.shape[1]))
    for _, rowdata in enumerate(pos):
        total += mat[rowdata[0], rowdata[1]]
        ans_mat[rowdata[0], rowdata[1]] = mat[rowdata[0], rowdata[1]]
    return total, ans_mat


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
    ans, ans_mat = ans_calculation(
        cost_matrix, ans_pos
    )  # Get the minimum or maximum value and corresponding matrix.

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
    ans, ans_mat = ans_calculation(
        profit_matrix, ans_pos
    )  # Get the minimum or maximum value and corresponding matrix.
    # Show the result
    print(f"Linear Assignment problem result: {ans:.0f}\n{ans_mat}")


if __name__ == "__main__":
    main()
