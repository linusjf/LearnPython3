#!/usr/bin/env python
"""
Algo_V3.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : algo_v3
# @created     : Monday Apr 03, 2023 21:31:37 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
from bisect import bisect_left
from hashlib import sha256
from struct import unpack_from

NODE_COUNT = 100
NEW_NODE_COUNT = 101
DATA_ID_COUNT = 10000000

node_range_starts = []
for node_id in range(NODE_COUNT):
    node_range_starts.append(DATA_ID_COUNT / NODE_COUNT * node_id)
new_node_range_starts = []
for new_node_id in range(NEW_NODE_COUNT):
    new_node_range_starts.append(DATA_ID_COUNT / NEW_NODE_COUNT * new_node_id)
MOVED_IDS = 0
for data_id in range(DATA_ID_COUNT):
    ID_DATA = str(data_id).encode("utf-8")
    hsh = unpack_from(">I", sha256(ID_DATA).digest())[0]
    node_id = bisect_left(node_range_starts, hsh % DATA_ID_COUNT) % NODE_COUNT
    new_node_id = bisect_left(new_node_range_starts, hsh % DATA_ID_COUNT) % NEW_NODE_COUNT
    if node_id != new_node_id:
        MOVED_IDS += 1
PERCENT_MOVED = 100.0 * MOVED_IDS / DATA_ID_COUNT
print(f"{MOVED_IDS:7d} ids moved, {PERCENT_MOVED:.02f}%")
