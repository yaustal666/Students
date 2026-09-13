#include <iostream>

int main() {
    int a = 0;
    float b = 2.2;
    
    if (false) {
        std::cout << b << std::endl;
    } else {
        std::cout << a << std::endl;
    }

    int n = 10;
    for (int i = 0; i < n; i += 2) {
        std::cout << b << std::endl;
    }

    int i = 0;
    while(i < 10) {
        std::cout << b << std::endl;
        i++;
    }
}