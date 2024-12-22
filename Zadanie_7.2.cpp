#include <iostream>
#include <set>
#include<list>

void calculateSum(int* arrA, int size) {
    
    std::set<int> mySet;

    for (int i = 0; i < size; i++) {
        if (arrA[i] >= -5 && arrA[i] <= 5) mySet.insert(arrA[i]);
    }
    std::list<int> myList(mySet.begin(), mySet.end());
    for (int elem: myList) {
        std::cout << elem<< " ";
    }
}

void findArrayWithMaxSum(int* arrA, int* arrB, int size) {
    

    setlocale(LC_ALL, "Rus");


    for (int i = 0; i < size; i++) {
        arrA[i] = arrA[i] - arrB[i];
    }
    std::cout << std::endl;
    calculateSum(arrA, size);
}

int main() {
    int N; // ������ ��������

    setlocale(LC_ALL, "Rus");

    // ���� ������� ��������
    std::cout << "������� ������ �������� (N): ";
    std::cin >> N;

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

    // ����� ������� � ���������� ������
    findArrayWithMaxSum(A, B, N);

    // ������������ ���������� ������
    delete[] A;
    delete[] B;

    return 0;
}