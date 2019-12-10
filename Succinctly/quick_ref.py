#!/usr/bin/env python
"""Quick reference example."""
# for timing
import time
# permutations, combinations
import itertools as it
# arrays, matrices, functions
import numpy as np
# determinant, inverse, etc.
import scipy.linalg as spla
# advanced functions like gamma
import scipy.special as ss
# math constants like e
import scipy.constants as sc
# functions for integration
import scipy.integrate as si
# functions for optimization
import scipy.optimize as so


class Permutation:
    """Define permutation class."""

    # custom class using an array

    def __init__(self, _n):
        """Construct class instance."""
        # constructor
        self._n = _n
        self._data = np.arange(_n)
        # [0, 1, 2, . . (n-1)]

    def as_string(self):
        """Return as string."""
        # instance method
        _s = "# "
        for i in range(self._n):
            # traverse an array
            _s += str(self._data[i]) + " "
        return _s + "#"

    @staticmethod
    def my_fact(_n):
        """Calculate factorial."""
        # static method
        _result = 1
        # iterative rather than recursive
        for i in range(1, _n + 1):
            # recursion supported in Python
            _result *= i
            # but usually not a good idea
        return _result

# ----------------------------------


def show_matrix(_m, _decimals):
    """Show matrix."""
    # standalone function
    (rows, cols) = np.shape(_m)
    # matrix dimensions as tuple
    for i in rows:
        # traverse a matrix
        for j in cols:
            print("%." + str(_decimals) % _m[i, j])
        print("")

def main():
    """Start program."""
    print("\nBegin quick ref demo \n")
    ARR_A = np.array([3.0, 2.0, 0.0, 1.0])
    # create array of float64
    ARR_B = np.zeros(4, dtype=np.int32)
    # create int array [0, 0, 0, 0]
    B = 1.0 in ARR_A
    # search array using "in": True
    RESULT = np.where(ARR_A == 1.0)
    # result is (array([3]),)
    ARR_S = np.sort(ARR_A, kind="quicksort")
    # sort array: [0.0, 1.0, 2.0, 3.0]
    ARR_R = ARR_S[::-1]
    # reverse: [3.0, 2.0, 1.0, 0.0]
    np.random.seed(0)
    # set seed for reproducibility
    np.random.shuffle(ARR_R)
    # randomize content order

    # copy array by reference
    ARR_REF = ARR_A
    # copy by view reference
    ARR_V = ARR_A.view()
    # copy array by value
    ARR_D = np.copy(ARR_A)
    ARR_E = ARR_A + ARR_B
    # add arrays

    M_A = np.matrix([[1.0, 2.0], [3.0, 4.0]])
    # matrix-style 2x2 matrix
    M_B = np.array([[8, 7], [6, 5]])
    # ndarray-style 2x2 matrix
    M_C = np.zeros((2, 2), dtype=np.int32)
    # ndarray 2x2 matrix all zeroes
    try:
        # try-except
        M = np.loadtxt("foo.txt")
        # matrix from file
    except ValueError as _e:
        print("Unable to open file: " + str(_e))

    M_E = M_A.transpose()
    # matrix transposition
    D = spla.det(M_A)

    # matrix determinant
    M_I = np.linalg.inv(M_A)
    # matrix inverse

    M_IDTY = np.eye(2)

    # identity 2x2 matrix
    M_M = np.dot(M_A, M_I)

    # matrix multiplication
    B = np.allclose(M_M, M_IDTY, 1.0e-5)
    # matrix equality by value
    M_X = M_A + np.array([5.0, 8.0])
    # broadcasting
    P_IT = it.permutations(range(3))
    # permutations iterator
    START_T = time.perf_counter()
    # timing
    for P in P_IT:
        print(P)
    END_T = time.perf_counter()
    ELAP = END_T - START_T
    print("elapsed = " + str(ELAP) + "secs")

    # string concatenation

    PC = Permutation(3)
    # instantiate a custom class
    print(PC.as_string())
    # instance method call
    NF = Permutation.my_fact(3)
    # static method call
    ARR = np.array([1.0, 3.0, 5.0, 7.0])

    # a sorted array
    II = np.searchsorted(ARR, 2.0)
    # binary search
    if II < len(ARR_S) and ARR_S[II] == 2.0:
        # somewhat tricky return
        print("2.0 found")

    (PERM, LOW, UPP) = spla.lu(M_A)
    # matrix LU decomposition
    MED = np.median(ARR_A)
    # statistics function
    RV = np.random.normal(0.0, 1.0)
    # random variable generation
    G = ss.gamma(3.5)
    # advanced math function

    print("\nEnd quick reference \n")


if __name__ == "__main__":
    main()
