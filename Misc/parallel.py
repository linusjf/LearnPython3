#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021  <@localhost>
#
# Distributed under terms of the MIT license.
from timebudget import timebudget
import math
import numpy as np
from multiprocessing import Pool

iterations_count = round(1e6)


def complex_operation(input_index):
    print("Complex operation. Input index: {:2d}".format(input_index))
    [math.exp(i) * math.sinh(i) for i in [1] * iterations_count]


@timebudget
def run_complex_operations(operation, input):
    for i in input:
        operation(i)


print("Serial. Without NumPy")
input = range(10)
run_complex_operations(complex_operation, input)


@timebudget
def run_complex_operations_p(operation, input, pool):
    pool.map(operation, input)


processes_count = 6

print("Parallel. Without NumPy")
processes_pool = Pool(processes_count)
run_complex_operations_p(complex_operation, range(10), processes_pool)


def complex_operation_numpy(input_index):
    print("Complex operation (numpy). Input index: {:2d}".format(input_index))
    data = np.ones(iterations_count)
    np.exp(data) * np.sinh(data)


print("Serial. With NumPy")
run_complex_operations(complex_operation_numpy, input)

print("Parallel. With NumPy")
processes_pool = Pool(processes_count)
run_complex_operations_p(complex_operation_numpy, input, processes_pool)
