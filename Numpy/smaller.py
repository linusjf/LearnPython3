#!/usr/bin/env python
# -*- coding: utf-8 -*-

from timeit import Timer

print(
    min(
        Timer(
            setup="""
import numpy as np
a = np.zeros((int(1e6),), dtype=np.float64)
""",
            stmt="""
a*a
""",
        ).repeat(5, 1000)
    )
)
print(
    min(
        Timer(
            setup="""
import numpy as np
b= np.zeros((int(1e6),), dtype=np.float32)
""",
            stmt="""
b*b
""",
        ).repeat(5, 1000)
    )
)
