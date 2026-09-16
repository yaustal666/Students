#include <iostream>
#include <cmath>

int main() {
    double x;
    std::cin >> x;

    int w = int(x);
    double v = x - w;

    if (w > v * 10) {
        x = x * 10;
    } else {
        x = x - v;
    }

    std::cout << "x: " << x << "\n";
}