#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021  <@localhost>
#
# Distributed under terms of the MIT license.

import math
import numpy as np
from timebudget import timebudget
import ipyparallel as ipp

iterations_count = round(1e6)

def complex_operation(input_index):
    print("Complex operation. Input index: {:2d}".format(input_index))
    [math.exp(i) * math.sinh(i) for i in [1] * iterations_count]

def complex_operation_numpy(input_index):
    print("Complex operation (numpy). Input index: {:2d}".format(input_index))
    data = np.ones(iterations_count)
    np.exp(data) * np.sinh(data)

@timebudget
def run_complex_operations(operation, input, pool):
    pool.map(operation, input)

cluster = ipp.Cluster.from_file()

rc = cluster.connect_client_sync()
rc.wait_for_engines(n=6)
print(rc.ids)

#rc[:].apply_sync(lambda: "Hello, World")
#client_ids = ipp.Client()
pool = rc[:]

input = range(10)
print('Without NumPy')
run_complex_operations(complex_operation, input, pool)
print('NumPy')
run_complex_operations(complex_operation_numpy, input, pool)
