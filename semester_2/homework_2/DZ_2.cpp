#include <iostream>
#include <cmath>

double simpson_rule(double (*f)(double), double a, double b, int n) {
    if (n % 2 == 1) n++; // Делаем n четным
    double h = (b - a) / n;
    double sum = f(a) + f(b);

    for (int i = 1; i < n; i += 2)
        sum += 4 * f(a + i * h);

    for (int i = 2; i < n-1; i += 2)
        sum += 2 * f(a + i * h);

    return (h / 3) * sum;
}

double function1(double x) {
    return x; // Интегрируемая функция
}

double function2(double x) {
    return -x + 6; // Интегрируемая функция
}

int main() {
    double result1 = simpson_rule(function1, 2, 3, 1);
    double result2 = simpson_rule(function2, 2, 3, 1);
    std::cout << "Приближенное значение интеграла: " << result2 - result1 << std::endl;
    return 0;
}