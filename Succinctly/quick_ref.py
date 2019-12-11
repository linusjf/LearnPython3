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
    
    # create array of float64
    arr_a = np.array([3.0, 2.0, 0.0, 1.0])

    print(arr_a)

    # create int array [0, 0, 0, 0]
    arr_b = np.zeros(4, dtype=np.int32)
    print(arr_b)

    # search array using "in": True
    _b = 1.0 in arr_a
    print(_b)

    # result is (array([3]),)
    _result = np.where(arr_a == 1.0)
    print(_result)
    # sort array: [0.0, 1.0, 2.0, 3.0]
    arr_s = np.sort(arr_a, kind="quicksort")
    print(arr_s)
    # reverse: [3.0, 2.0, 1.0, 0.0]
    arr_r = arr_s[::-1]
    print(arr_r)
    # set seed for reproducibility
    np.random.seed(0)
    # randomize content order
    np.random.shuffle(arr_r)

    # copy array by reference
    arr_ref = arr_a
    # copy by view reference
    arr_v = arr_a.view()
    # copy array by value
    arr_d = np.copy(arr_a)
    # add arrays
    arr_e = arr_a + arr_b

    # matrix-style 2x2 matrix
    m_a = np.matrix([[1.0, 2.0], [3.0, 4.0]])
    m_b = np.array([[8, 7], [6, 5]])
    # ndarray-style 2x2 matrix
    m_c = np.zeros((2, 2), dtype=np.int32)
    # ndarray 2x2 matrix all zeroes
    try:
        # try-except
        _m = np.loadtxt("foo.txt")
        # matrix from file
    except IOError as _e:
        print("Unable to open file: " + str(_e))

    # matrix transposition
    m_e = m_a.transpose()
    # matrix determinant
    _d = spla.det(m_a)

    # matrix inverse
    m_i = np.linalg.inv(m_a)

    # identity 2x2 matrix
    m_idty = np.eye(2)

    # matrix multiplication
    m_m = np.dot(m_a, m_i)

    # matrix equality by value
    _b = np.allclose(m_m, m_idty, 1.0e-5)
    # broadcasting
    m_x = m_a + np.array([5.0, 8.0])
    
    # permutations iterator
    p_it = it.permutations(range(3))
    start_t = time.perf_counter()
    # timing
    for _p in p_it:
        print(_p)
    end_t = time.perf_counter()
    _elap = end_t - start_t
    # string concatenation
    print("elapsed = " + str(_elap) + "secs")


    # instantiate a custom class
    _pc = Permutation(3)
    # instance method call
    print(_pc.as_string())
    # static method call
    _nf = Permutation.my_fact(3)
    _arr = np.array([1.0, 3.0, 5.0, 7.0])

    # a sorted array
    _ii = np.searchsorted(_arr, 2.0)
    # binary search
    if _ii < len(arr_s) and arr_s[_ii] == 2.0:
        # somewhat tricky return
        print("2.0 found")

    # matrix LU decomposition
    (_perm, _low, _upp) = spla.lu(m_a)
    # statistics function
    _med = np.median(ARR_A)
    # random variable generation
    _rv = np.random.normal(0.0, 1.0)
    # advanced math function
    g = ss.gamma(3.5)

    print("\nEnd quick reference \n")


if __name__ == "__main__":
    main()
