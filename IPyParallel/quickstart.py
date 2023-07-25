#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021  <@localhost>
#
# Distributed under terms of the MIT license.

import time
import ipyparallel as ipp

task_durations = [1] * 25
# request a cluster
with ipp.Cluster() as rc:
    # get a view on the cluster
    view = rc.load_balanced_view()
    # submit the tasks
    asyncresult = view.map_async(time.sleep, task_durations)
    # wait interactively for results
    asyncresult.wait_interactive()
    # retrieve actual results
    result = asyncresult.get()
# at this point, the cluster processes have been shutdown
