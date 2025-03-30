#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <ctime>

void countingSort(std::vector<int>& arr, int exp) {
    std::vector<int> output(arr.size());
    int count[10] = {0};
    
    for (int num : arr)
        count[(num / exp) % 10]++;
    
    for (int i = 1; i < 10; i++)
        count[i] += count[i - 1];
    
    for (int i = arr.size() - 1; i >= 0; i--) {
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }
    
    arr = output;
}

void radixSort(std::vector<int>& arr) {
    int maxNum = *std::max_element(arr.begin(), arr.end());
    
    for (int exp = 1; maxNum / exp > 0; exp *= 10)
        countingSort(arr, exp);
}

int main() {
    std::srand(std::time(0));
    int size = 1000 + std::rand() % 9001;
    std::vector<int> arr(size);
    
    // Генерация случайных чисел от 1 до 10 000 000
    for (int& num : arr)
        num = 1 + std::rand() % 10000000;
    
    std::clock_t start = std::clock();
    radixSort(arr);
    std::clock_t end = std::clock();
    
    double duration = (double)(end - start) / CLOCKS_PER_SEC;
    std::cout << "Sorting time: " << duration << " seconds" << std::endl;
    
    for (int num : arr)
        std::cout << num << " ";
    std::cout << std::endl;
    std::cout << "Array size: " << size << std::endl;
    
    return 0;
}
