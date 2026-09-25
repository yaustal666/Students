#include <iostream>

int main() {
    int k;
    std::cin >> k;

    int res = 0;
    // For
    for (int i = 1; i < k; i++) {
        res += (i + 1) * (i + 1);
    }
    std::cout << "Cycle for: " << res << "\n";

    // While
    int n = 1;
    res = 0;
    while (n < k) {
        res += (n + 1) * (n + 1);
        n++;
    }
    std::cout << "Cycle while: " << res << "\n";

    // Do while
    n = 1;
    res = 0;
    do {
        res += (n + 1) * (n + 1);
        n++;
    } while (n < k);
    std::cout << "Cycle do while: " << res << "\n";
}