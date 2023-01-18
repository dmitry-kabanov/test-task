from optimize import SteepestDescent
from optimize.functionals import parabola_nd


def main():
    opt = SteepestDescent(verbose=False)
    x0 = (2.0, 1.0, 5.0)
    xmin = opt.minimize(parabola_nd, x0)

    print(f"xmin: {xmin}")
    if opt.reason == opt.CONVERGENCE:
        print("Reason of optimization end: convergence")
    elif opt.reason == opt.MAX_ITERATIONS:
        print("Reason of optimization end: exceed number of max iterations")
    else:
        raise Exception("Unknown optimization error")


if __name__ == "__main__":
    main()
