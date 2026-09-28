#include <iostream>

int main() {
    int x, y, z, k, m;
    std::cin >> x >> y >> z >> k >> m;

    bool A, B, C, D;
    A = m % 3 == 1;
    B = (x * z * y != 2);
    C = (k / 2 >= 5);
    D = true;

    bool L = !((A || B) && C) == ((!B) && D);

    if (L) {
        std::cout << "true" << std::endl;
    } else {
        std::cout << "false" << std::endl;
    }
}