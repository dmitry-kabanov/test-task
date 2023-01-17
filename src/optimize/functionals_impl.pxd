# distutils: language = c++
# cython: language_level = 3
from libcpp.vector cimport vector


cdef extern from "functionals_impl.hpp" namespace "optim":
    double parabola_1d(double x)
    double parabola_nd(vector[double] x)
