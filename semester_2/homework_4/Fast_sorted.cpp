#include <iostream>
#include <vector>
#include <thread>
#include <random>
#include <chrono>
#include <cmath>
#include <atomic>

using namespace std;

int max_threads;
atomic<int> active_threads(0);

void quicksort(vector<int>& arr, int left, int right, int depth) {
    if (left >= right) return;
    
    int pivot = arr[(left + right) / 2];
    int i = left, j = right;
    
    while (i <= j) {
        while (arr[i] < pivot) ++i;
        while (arr[j] > pivot) --j;
        if (i <= j) {
            swap(arr[i], arr[j]);
            ++i;
            --j;
        }
    }
    
    bool do_parallel = (depth < log2(max_threads)) && (active_threads.load() < max_threads);
    
    if (do_parallel) {
        active_threads += 2;
        
        thread t1([&arr, left, j, depth]() {
            quicksort(arr, left, j, depth + 1);
            active_threads--;
        });
        
        thread t2([&arr, i, right, depth]() {
            quicksort(arr, i, right, depth + 1);
            active_threads--;
        });
        
        t1.join();
        t2.join();
    } else {
        quicksort(arr, left, j, depth + 1);
        quicksort(arr, i, right, depth + 1);
    }
}

int main() {
    int quantity_element;
    cout << "Введите количество элементов: ";
    cin >> quantity_element;
    
    cout << "Введите количество потоков: ";
    cin >> max_threads;
    
    vector<int> arr;
    arr.reserve(quantity_element);
    
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> dist(1, 100000);
    
    for (int i = 0; i < quantity_element; i++)
        arr.push_back(dist(gen));
    
    auto start = chrono::high_resolution_clock::now();
    
    quicksort(arr, 0, arr.size() - 1, 0);
    
    auto stop = chrono::high_resolution_clock::now();
    chrono::duration<double> duration = stop - start;
    
    cout << "Время сортировки: " << duration.count() << " секунд" << endl;
    
    return 0;
}
