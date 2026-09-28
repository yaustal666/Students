#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>

int main() {
    double a, R;
    std::cin >> a >> R;
    double pi = M_PI;
    double t =  (4 / (3 * a * a)) * (R*R*R + a*R*R + R*a*a);
    double twopiR = 2 * pi * R;
    
    double L = (twopiR + t) * std::pow(std::cos(t), 2);
    
    std::cout << L << std::endl;
}