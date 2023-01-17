import numpy as np
import pytest

from optimize.functionals import parabola_1d, parabola_nd


class TestParabola1D:
    def test_works_with_scalars(self):
        assert parabola_1d(0.0) == 0.0
        assert parabola_1d(1.0) == 1.0
        assert parabola_1d(3.0) == 9.0

    def test_works_trivial_ndarrays(self):
        assert parabola_1d(np.array([0.0])) == 0.0
        assert parabola_1d(np.array([1.0])) == 1.0
        assert parabola_1d(np.array([3.0])) == 9.0

    def test_does_not_work_with_lists(self):
        with pytest.raises(TypeError):
            parabola_1d([1.0])


class TestParabolaND:
    def test_works_with_ndarrays(self):
        assert parabola_nd(np.array([1.0])) == 1.0
        assert parabola_nd(np.array([1.0, 2.0])) == 5.0
        assert parabola_nd(np.array([1.0, 2.0, 3.0])) == 14.0

    def test_does_not_work_with_lists(self):
        with pytest.raises(TypeError):
            parabola_nd([1.0, 2.0])
