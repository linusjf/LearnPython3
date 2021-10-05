#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021  <@localhost>
#
# Distributed under terms of the MIT license.
import ipyparallel as ipp

# start cluster, connect client
with ipp.Cluster(n=4) as rc:
    print(rc)
    e_all = rc[:]
    print(e_all)
    ar = e_all.apply(lambda x, y: x**2 + y**2, 5, 12)
    print(ar)
    rc.wait_interactive()
    results = ar.get()
    print(results)
# have results, cluster is shutdown
