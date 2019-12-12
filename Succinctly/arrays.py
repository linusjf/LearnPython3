#!/usr/bin/env python
"""Arrays demo."""
import numpy as np


def my_print(arr, cols, dec):
    """Print array."""
    _n = len(arr)
    # print array using indexing
    fmt = "%." + str(dec) + "f"
    # like %.4f
    for i in range(_n):
        # alt: for x in arr
        if i > 0 and i % cols == 0:
            print("")
        print(fmt % arr[i] + ",")
    print("")

# =====


def main():
    """Run main program."""
    print("\nBegin array demo \n")
    print("Creating array arr using np.array() & list with hard-coded values")
    arr = np.array([1., 3., 5., 7., 9.])
    # float64
    _dt = np.dtype(arr[0])
    print("Cell element type is " + str(_dt.name))
    print("")

    print("Printing array arr using built-in print() ")
    print(arr)
    print("")

    print("Creating int array arr using np.arange(9) ")
    arr = np.arange(9)
    # [0, 1, . . 8]
    # int32
    print("Printing array arr using built-in print() ")
    print(arr)
    print("")

    cols = 4
    dec = 0
    print("Printing array arr using my_print() with cols=" + str(cols))
    print("and dec=" + str(dec))
    my_print(arr, cols, dec)

    print("Creating array arr using np.zeros(5) ")
    arr = np.zeros(5)
    print("Printing array arr using built-in print() ")
    print(arr)
    print("")

    print("Creating array arr using  np.linspace(2., 5., 6)")
    arr = np.linspace(2., 5., 6)
    # 6 values from [2.0 to 5.0] inc.
    print("Printing array arr using built-in print() ")
    print(arr)
    print("")

    print("\nEnd demo \n")

if __name__ == "__main__":
    main()
