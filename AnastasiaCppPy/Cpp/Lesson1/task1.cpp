#include <iostream>
#include <cmath>

int main() {
    double A, B, Z;
    std::cin >> A >> B;

    double up = std::sqrt(std::abs(A) + std::pow((A + B), 2));
    double down = A * B;
    double frac = up / down;

    Z = B * (std::tan(frac) + std::exp(frac));

    std::cout << Z << std::endl;
}