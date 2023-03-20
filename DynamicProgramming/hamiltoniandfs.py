#!/usr/bin/env python
"""
Hamiltoniandfs.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : hamiltoniandfs
# @created     : Monday Mar 20, 2023 11:06:28 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
NOT_IN_STACK = 0
IN_STACK = 1


def dfs(vertex, adj, labels, instack_count):
    """Search depth first."""
    size = len(adj)
    if instack_count == size:
        return True
    for i in range(size):
        if adj[vertex][i] and labels[i] == NOT_IN_STACK:
            labels[i] = IN_STACK
            if dfs(i, adj, labels, instack_count + 1):
                return True
            labels[i] = NOT_IN_STACK
    return False


def check_using_dfs(adj):
    """Check using depth first search."""
    size = len(adj)
    labels = [-1] * size
    for i in range(size):
        labels[i] = NOT_IN_STACK
        for i in range(size):
            labels[i] = IN_STACK
            if dfs(i, adj, labels, 1):
                return True
            labels[i] = NOT_IN_STACK
        return False


# Driver Code
ADJ = [[0, 1, 1, 1, 0], [1, 0, 1, 0, 1], [1, 1, 0, 1, 1], [1, 0, 1, 0, 0]]
print(check_using_dfs(ADJ))
