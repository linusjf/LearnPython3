#!/usr/bin/env python
"""Display structure."""
import numpy as np

def make_x(_n):
    """Make result."""
    result = np.zeros((_n, _n))
    for i in range(_n):
        for j in range(_n):
            if i == j or (i + j == _n-1):
                result[i, j] = 1.0
    return result

def main():
    """Start program."""
    print("\nBegin program structure demo \n")

    try:
        _n = 5
        print("X matrix with size n = " + str(_n) + " is ")
        _mx = make_x(_n)
        print(_mx)
        print("")

        _n = -1
        print("X matrix with size n = " + str(_n) + " is ")
        _mx = make_x(_n)
        print(_mx)
        print("")
    except ValueError as _e:
        print("Error: " + str(_e))
        print("Error: " + str(type(_e)))

    print("\nEnd demo \n")

if __name__ == "__main__":
    main()
