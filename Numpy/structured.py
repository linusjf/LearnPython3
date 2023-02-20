#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

samples = np.zeros((6,), dtype=[("sensor_code", "S4"), ("position", float), ("value", float)])
print(samples.ndim)
print(samples.shape)
print(samples.dtype.names)
samples[:] = [
    ("ALFA", 1, 0.37),
    ("BETA", 1, 0.11),
    ("TAU", 1, 0.13),
    ("ALFA", 1.5, 0.37),
    ("ALFA", 3, 0.11),
    ("TAU", 1.2, 0.13),
]
print(samples)
print(samples["sensor_code"])
print(samples["value"])
print(samples[0])
samples[0]["sensor_code"] = "TAU"
print(samples[0])
print(samples[["position", "value"]])
print(samples[samples["sensor_code"] == b"ALFA"])
