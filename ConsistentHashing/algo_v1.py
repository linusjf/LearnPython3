#!/usr/bin/env python
"""
AlgoV1.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : algo_v1
# @created     : Monday Apr 03, 2023 18:14:16 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
from hashlib import sha256
from struct import unpack_from
from random import SystemRandom

NODE_COUNT = 100
DATA_ID_COUNT = 10000000
DESIRED_COUNT = DATA_ID_COUNT / NODE_COUNT

node_counts = [0] * NODE_COUNT
for data_id in range(DATA_ID_COUNT):
    ID_DATA = str(data_id).encode("utf-8")
    # This just pulls part of the hash out as an integer
    hsh = unpack_from(">I", sha256(ID_DATA).digest())[0]
    node_id = hsh % NODE_COUNT
    node_counts[node_id] += 1
print(f"{DESIRED_COUNT}: Desired data ids per node")
max_count = max(node_counts)
over = 100.0 * (max_count - DESIRED_COUNT) / DESIRED_COUNT
print(f"{max_count}: Most data ids on one node, {over}% over")
min_count = min(node_counts)
under = 100.0 * (DESIRED_COUNT - min_count) / DESIRED_COUNT
print(f"{min_count}: Least data ids on one node, {under}% under")
node_counts = [0] * NODE_COUNT
cryptogen = SystemRandom()
for _ in range(DATA_ID_COUNT):
    ID_DATA = str(cryptogen.random() * DATA_ID_COUNT).encode("utf-8")
    # This just pulls part of the hash out as an integer
    hsh = unpack_from(">I", sha256(ID_DATA).digest())[0]
    node_id = hsh % NODE_COUNT
    node_counts[node_id] += 1
print(f"{DESIRED_COUNT}: Desired data ids per node")
max_count = max(node_counts)
over = 100.0 * (max_count - DESIRED_COUNT) / DESIRED_COUNT
print(f"{max_count}: Most data ids on one node, {over}% over")
min_count = min(node_counts)
under = 100.0 * (DESIRED_COUNT - min_count) / DESIRED_COUNT
print(f"{min_count}: Least data ids on one node, {under}% under")
