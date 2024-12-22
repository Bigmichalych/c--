#include <iostream>

void calculate(int* arrA, int* arrB, int size, int minA, int minB) {

    for (int i = 0; i < size; i++) {
        arrA[i] = arrA[i]/minA;
    }
    std::cout << "Массив А после деления на его же наименьшее значение: ";
    for (int i = 0; i < size; i++) {
        std::cout << arrA[i] << " ";
    }
    std::cout << std::endl;

    for (int i = 0; i < size; i++) {
        arrB[i] = arrB[i] / minB;
    }
    std::cout << "Массив B после деления на его же наименьшее значение: ";
    for (int i = 0; i < size; i++) {
        std::cout << arrB[i] << " ";
    }
    std::cout << std::endl;
}

void findArrayWithMin(int* arrA, int* arrB, int size) {
    int minA = arrA[0], minB = arrB[0];

    setlocale(LC_ALL, "Rus");

    for (int i = 1; i < size; i++) {
        if (minA > arrA[i]) minA = arrA[i];
    }
    for (int i = 1; i < size; i++) {
        if (minB > arrB[i]) minB = arrB[i];
    }
    calculate(arrA, arrB, size, minA, minB);
    
    std::cout << std::endl;
}

int main() {
    int N = 5; // Размер массивов

    setlocale(LC_ALL, "Rus");

    int* A = new int[N]; // Динамическое выделение памяти для массива A
    int* B = new int[N]; // Динамическое выделение памяти для массива B

    // Ввод массивов
    std::cout << "Введите " << N << " элементов для массива A:" << std::endl;
    for (int i = 0; i < N; i++) {
        std::cin >> A[i];
    }

    std::cout << "Введите " << N << " элементов для массива B:" << std::endl;
    for (int i = 0; i < N; i++) {
        std::cin >> B[i];
    }

    findArrayWithMin(A, B, N);

    // Освобождение выделенной памяти
    delete[] A;
    delete[] B;

    return 0;
}