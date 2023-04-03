#!/usr/bin/env python
"""
AlgoV2.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : algo_v2
# @created     : Monday Apr 03, 2023 21:01:31 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
from hashlib import sha256
from struct import unpack_from

NODE_COUNT = 100
NEW_NODE_COUNT = 101
DATA_ID_COUNT = 10000000

MOVED_IDS = 0
for data_id in range(DATA_ID_COUNT):
    ID_DATA = str(data_id).encode("utf-8")
    hsh = unpack_from(">I", sha256(ID_DATA).digest())[0]
    node_id = hsh % NODE_COUNT
    new_node_id = hsh % NEW_NODE_COUNT
    if node_id != new_node_id:
        MOVED_IDS += 1
PERCENT_MOVED = 100.0 * MOVED_IDS / DATA_ID_COUNT
print(f"{MOVED_IDS} ids moved, {PERCENT_MOVED:03.2f}%")
