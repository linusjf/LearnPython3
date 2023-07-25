#!/usr/bin/env python
import ipyparallel as ipp

rc = ipp.Cluster(n=4).start_and_connect_sync()
rc.wait_for_engines(n=4)
print(rc.ids)
print(rc[:].apply_sync(lambda: "Hello, World"))
