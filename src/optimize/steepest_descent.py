import numpy as np

from .compute_gradient import compute_gradient


class SteepestDescent:
    CONVERGENCE = 0
    MAX_ITERATIONS = 1

    def __init__(self, step_size=1e-1, max_iter=1000, tol=1e-6, verbose=True):
        self.step_size = step_size
        self.max_iter = max_iter
        self.tol = tol
        self.history = []
        self.verbose = verbose

    def minimize(self, f, x0):
        x = x0
        i = 0
        for i in range(self.max_iter):
            df_dx = compute_gradient(f, x)
            x_new = x - self.step_size * df_dx
            if self.verbose:
                print(f"x_new = {x_new}")
            self.history.append(x)
            if np.linalg.norm(x_new - x, 2) < self.tol:
                self.reason = self.CONVERGENCE
                if self.verbose:
                    print("Convergence")
                return x_new

            x = x_new

        self.reason = self.MAX_ITERATIONS
        if self.verbose:
            print("Maximum number of iterations reached")

        return x
