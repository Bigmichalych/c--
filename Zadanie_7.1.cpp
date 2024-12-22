#include <iostream>

void calculate(int* arrA, int* arrB, int size, int minA, int minB) {

    for (int i = 0; i < size; i++) {
        arrA[i] = arrA[i]/minA;
    }
    std::cout << "������ � ����� ������� �� ��� �� ���������� ��������: ";
    for (int i = 0; i < size; i++) {
        std::cout << arrA[i] << " ";
    }
    std::cout << std::endl;

    for (int i = 0; i < size; i++) {
        arrB[i] = arrB[i] / minB;
    }
    std::cout << "������ B ����� ������� �� ��� �� ���������� ��������: ";
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
    int N = 5; // ������ ��������

    setlocale(LC_ALL, "Rus");

    int* A = new int[N]; // ������������ ��������� ������ ��� ������� A
    int* B = new int[N]; // ������������ ��������� ������ ��� ������� B

    // ���� ��������
    std::cout << "������� " << N << " ��������� ��� ������� A:" << std::endl;
    for (int i = 0; i < N; i++) {
        std::cin >> A[i];
    }

    std::cout << "������� " << N << " ��������� ��� ������� B:" << std::endl;
    for (int i = 0; i < N; i++) {
        std::cin >> B[i];
    }

    findArrayWithMin(A, B, N);

    // ������������ ���������� ������
    delete[] A;
    delete[] B;

    return 0;
}