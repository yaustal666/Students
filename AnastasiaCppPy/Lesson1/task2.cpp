#include <iostream>

int main() {
    double y0;
    std::cin >> y0;

    double x, y;
    std::cin >> x >> y;

    bool Area1 = (x < 0) && 
                 (y > 0) && 
                 (y > (-(x * x) + std::abs(y0)));
    
    bool Area2 = (x < 0) &&
                 (y < 0) &&
                 (y < (-(x * x) + std::abs(y0))) &&
                 (y > x);
    
    bool Area3 = (x > 0) &&
                 (y < (-(x * x) + std::abs(y0)));
    
    bool result = Area1 || Area2 || Area3;
    if (result) {
        std::cout << "\nTochka popadaet";
    } else {
        std::cout << "\nTochka ne popadaet";
    }
}