#include <iostream>

int main() {
    double x = -4;
    double res = 0;

    // For
    double a;
    std::cin >> a;
    std::cout << "For cycle:\n";
    for (;x <= 5; x++) {
        double up = (2*x + a);
        double down = (x*x*x - 2*x*x - x + 2);
        if (down == 0) {
            std::cout << "x = " << x << " cant evaluate\n";
        } else {
            std::cout << "x = " << x << " result: " << up / down << "\n";
        }
    }

    // While
    std::cout << "\nWhile cycle:\n";
    x = -4;
    while (x <= 5) {
        double up = (2*x + a);
        double down = (x*x*x - 2*x*x - x + 2);
        if (down == 0) {
            std::cout << "x = " << x << " cant evaluate\n";
        } else {
            std::cout << "x = " << x << " result: " << up / down << "\n";
        }
        x++;
    }

    // Do while
    std::cout << "\nDo while cycle:\n";
    x = -4;
    do {
        double up = (2*x + a);
        double down = (x*x*x - 2*x*x - x + 2);
        if (down == 0) {
            std::cout << "x = " << x << " cant evaluate\n";
        } else {
            std::cout << "x = " << x << " result: " << up / down << "\n";
        }
        x++;
    } while (x <= 5);
}