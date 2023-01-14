import numpy as np
import numpy.testing as npt

from optimize import SteepestDescent


def test_1():
    def f(x):
        return (x[0] - 1) ** 2 + (x[1] - 2) ** 2

    x = np.array([3.0, 3.0])
    gd = SteepestDescent()
    xmin = gd.minimize(f, x)
    desired = np.array([1.0, 2.0])

    npt.assert_allclose(xmin, desired, rtol=1e-4, atol=1e-8)
