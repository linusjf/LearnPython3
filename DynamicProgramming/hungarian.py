#!/usr/bin/env python
"""Hungarian Algorithm."""
#
# @file        : hungarian
# @created     : Saturday Mar 18, 2023 16:20:07 IST
# https://python.plainenglish.io/hungarian-algorithm-introduction-python-implementation-93e7c0890e15
# -*- coding: utf-8 -*-"
######################################################################
import numpy as np


def min_zero_row(zero_mat, mark_zero):
    """Compute min zero row."""
    # The function can be split into two steps:
    # 1 The function is used to find the row which containing the fewest 0.
    # 2 Select the zero number on the row, and then mark the
    # corresponding row and column as False

    # Find the row
    min_row = [99999, -1]

    for row_num in range(zero_mat.shape[0]):
        row_sum = np.sum(zero_mat[row_num])
        if row_sum and min_row[0] > row_sum:
            min_row = [row_sum, row_num]

    # minimum row found
    print(f"min_row = {min_row}")
    sel_row = min_row[1]
    # Mark the specific row and column as False
    col = np.where(zero_mat[sel_row])
    print(f"col index indices = {col}")
    col = col[0][0]
    print(f"col = {col}")
    mark_zero.append((sel_row, col))
    # mask row and column
    zero_mat[sel_row, :] = False
    zero_mat[:, col] = False


def mark_matrix(mat):
    """Find the returning possible solutions for LAP problem."""
    # Transform the matrix to boolean matrix(0 = True, others = False)
    cur_mat = mat
    zero_bool_mat = cur_mat == 0
    zero_bool_mat_copy = zero_bool_mat.copy()

    # Recording possible answer positions by marked_zero
    marked_zero = []
    while True in zero_bool_mat_copy:
        min_zero_row(zero_bool_mat_copy, marked_zero)

    # Recording the row and column positions separately.
    marked_zero_row = []
    for _, row in enumerate(marked_zero):
        marked_zero_row.append(row[0])

    # Step 2-2-1
    non_marked_row = list(set(range(cur_mat.shape[0])) - set(marked_zero_row))
    print(f"non-marked-row = {non_marked_row}")
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


def hungarian_algorithm(mat):  # noqa
    """Solve Hungarian algorithm."""
    dim = mat.shape[0]
    print(f"dim = {dim}")
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
        print(f"zero_count = {zero_count}")

        if zero_count < dim:
            cur_mat = adjust_matrix(cur_mat, marked_rows, marked_cols)

    return ans_pos


def ans_calculation(mat, pos):  # noqa
    """Calculate answer."""
    total = 0
    ans_mat = np.zeros((mat.shape[0], mat.shape[1]))
    for _, rowdata in enumerate(pos):
        total += mat[rowdata[0], rowdata[1]]
        ans_mat[rowdata[0], rowdata[1]] = mat[rowdata[0], rowdata[1]]
    return total, ans_mat
