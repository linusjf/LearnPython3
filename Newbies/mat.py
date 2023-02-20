#!/usr/bin/env python3
"""MATLAB file format."""
import numpy as np
from scipy import io as sio

ARRAY = np.ones((4, 4))
sio.savemat("example.mat", {"array": ARRAY})
DATA = sio.loadmat("example.mat", struct_as_record=True)
print(DATA["array"])
