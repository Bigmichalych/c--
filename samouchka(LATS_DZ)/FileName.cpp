#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <numbers>
using namespace std;

float TwoFunk(float x, float y) {
    if (y == 0) {
        cout << "ERROR: Division by zero" << endl;
        throw invalid_argument("Division by zero");
    }
    float r = cos(x / y);
    float s = pow(2, -3 * x) + pow(M_PI * y, 1 / 3);
    float c = max(r, s);
    return c;
}

int main() {
    setlocale(LC_CTYPE, "rus");
    float x, y;
    cin >> x >> y;
    cout << TwoFunk(x, y);
    return 0;
}