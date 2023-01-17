import numpy as np
import numpy.testing as npt

from optimize import SteepestDescent


def convex_function(xstar=[1.0, 2.0]):
    def f(x):
        return np.sum(np.square(x - xstar))

    return f


def test_steepest_descent__2d_convex_case__minimizes_well():
    x0 = np.array([3.0, 3.0])
    xstar = np.array([1.0, 2.0])

    xmin = SteepestDescent().minimize(convex_function(xstar), x0)

    npt.assert_allclose(xmin, xstar, rtol=1e-4, atol=1e-8)


def test_steepest_descent__2d_convex_case__one_step_decreases_function_value():
    x0 = np.random.random(size=(2,))
    f = convex_function()

    x1 = SteepestDescent(max_iter=1).minimize(f, x0)

    assert f(x1) < f(x0)


def test_steepest_descent__ND_convex_case__minimizes_well():
    N = 5
    xstar = np.random.normal(loc=np.arange(N), scale=7, size=(N,))
    x0 = np.random.normal(loc=0.0, scale=3, size=(N,))
    f = convex_function(xstar)

    xmin = SteepestDescent().minimize(f, x0)

    npt.assert_allclose(xmin, xstar, rtol=1e-4, atol=1e-8)
