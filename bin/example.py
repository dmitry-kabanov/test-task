from optimize import SteepestDescent
from optimize.functionals import parabola_nd


def main():
    opt = SteepestDescent(step_size=1e-1, tol=1e-6, verbose=True)
    x0 = (2.0, 1.0, 5.0)
    xmin = opt.minimize(parabola_nd, x0)

    print(f"xmin: {xmin}")
    assert opt.status == opt.CONVERGENCE


if __name__ == "__main__":
    main()
