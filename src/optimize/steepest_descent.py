import numpy as np

from .compute_gradient import compute_gradient


class SteepestDescent:
    r"""Steepest descent method with fixed step size.

    Optimizes a given functional by moving in the direction of the steepest
    descent, by estimating the gradient of the functional numerically:

    .. math::

    x_{k+1} = x_k - \alpha \grad f(x_k)

    Usage
    -----
    >>> opt = SteepestDescent()
    >>> x0 = [1.0, 2.0]
    >>> f = lambda x: x[0]**2 + x[1]**2
    >>> xmin = opt.minimize(f, x0)

    Attributes
    ----------
    history : list of ndarrays of shape (n,)
        History of values of :math:`x` during optimization process.
    status : int
        Status of the terminated optimization process. See class attributes
        `CONVERGENCE` and `MAX_ITERATIONS`.
    f_value : float
        The value of the objective functional after the termination
        of the optimization process.

    Parameters
    ----------
    step_size : float
        Fixed step size (:math:`\alpha` in the above formula).
    max_iter : int
        Maximum number of iterations allowed for the optimization process.
    tol : float
        Tolerance for determing if the optimization process has converged.
        Precisely, it computes the L2-norm in difference between
        :math:`x_{n+1}` and :math:`x`.
    verbose : bool
        If true, print optimization information to screen.

    """

    CONVERGENCE = 1
    MAX_ITERATIONS = 2

    def __init__(self, step_size=1e-1, max_iter=1000, tol=1e-6, verbose=True):
        self.step_size = step_size
        self.max_iter = max_iter
        self.tol = tol
        self.verbose = verbose
        self.history = []
        self.status = None
        self.f_value = None

    def minimize(self, f, x0):
        """Minimize functional `f` using initial guess `x0`.

        Parameters
        ----------
        f : callable
            The objective to be minimized, :math:`f: R^n -> R`.
        x0 : ndarray|list of floats of shape (n,)
            Initial guess to start the optimization process.

        Returns
        -------
        ndarray of floats of shape (n,)
            Updated value of the initial guess.
        """
        x = x0
        i = 0
        for i in range(self.max_iter):
            df_dx = compute_gradient(f, x)
            x_new = x - self.step_size * df_dx
            self.history.append(x)
            if np.linalg.norm(x_new - x, 2) < self.tol:
                self.status = self.CONVERGENCE
                x = x_new
                break

            x = x_new

        self.f_value = f(x)

        if not self.status:
            self.status = self.MAX_ITERATIONS

        if self.verbose:
            self._print_report()

        return x

    def _print_report(self):
        if self.status == self.CONVERGENCE:
            print("Success: optimization convergence")
        else:
            print("Warning: Maximum number of iterations reached")

        print(f"Number of iterations: {len(self.history)}")
        print(f"Value of the function: {self.f_value}")
