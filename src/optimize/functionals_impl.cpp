#include <cmath>
#include <vector>

#include "functionals_impl.hpp"


namespace optim {

double parabola_1d(double x) {
    return std::pow(x, 2);
}

double parabola_nd(std::vector<double> x) {
    double sum = 0.0;
    for (auto & el : x) {
        sum += el * el;
    }

    return sum;
}

}
