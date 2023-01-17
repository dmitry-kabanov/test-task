# cython: language_level = 3
from libcpp.vector cimport vector

cimport optimize.functionals_impl as f


def parabola_1d(x):
    return f.parabola_1d(x)


def parabola_nd(double[::1] x):
    cdef vector[double] xvec
    xvec.assign(&x[0], &x[0] + len(x))
    return f.parabola_nd(xvec)
