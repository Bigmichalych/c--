#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>

int main()
{
    float x, y;
    std::cout << "Input x and y values: ";
    std::cin >> x >> y;

    double R = cos(x / y);
    double S = pow(2, -3 * x) + pow(M_PI * y, 1 / 3);
    double C = std::max(R, S);


    std::cout << "R = " << R << "\n";
    std::cout << "S = " << S << "\n";
    std::cout << "C = " << C << "\n";

    std::cout << "Press Enter to end...";
    system("pause");

    return 0;
}