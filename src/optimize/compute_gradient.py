from typing import Callable

import numpy as np


def compute_gradient(f: Callable, x: np.ndarray) -> np.ndarray:
    """Compute the gradient of function `f` with respect to the input vector `x`."""
    eps = 1e-8
    xplus = np.copy(x)
    xminus = np.copy(x)
    df_dx = np.zeros_like(x)
    for i in range(len(x)):
        x_i = x[i]
        dx = x[i] * eps
        xplus[i] = xplus[i] + dx
        xminus[i] = xminus[i] - dx
        df_dx[i] = (f(xplus) - f(xminus)) / (2 * dx)
        xplus[i] = x_i
        xminus[i] = x_i

    return df_dx
