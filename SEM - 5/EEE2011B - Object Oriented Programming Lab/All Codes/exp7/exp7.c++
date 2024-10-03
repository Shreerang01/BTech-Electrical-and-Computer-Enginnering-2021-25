/*
Problem statement:
   Perform bubble sort operation using the template for integer and floating data types

Author: Shreerang P Mhatre
Date: 27/09/2023

*/

#include <iostream>
#include <vector>

template <typename T>
void bubbleSort(std::vector<T> &arr) {
    int n = arr.size();
    bool swapped;

    do {
        swapped = false;
        for (int i = 0; i < n - 1; ++i) {
            if (arr[i] > arr[i + 1]) {
                std::swap(arr[i], arr[i + 1]);
                swapped = true;
            }
        }
    } while (swapped);
}

int main() {
    // Sorting integers
    std::vector<int> intArr = {7,10,888,2,3};
    std::cout << "Original integer array: ";

    for (const int &num : intArr) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    bubbleSort(intArr);

    std::cout << "Sorted integer array: ";
    for (const int &num : intArr) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    // Sorting floats
    std::vector<float> floatArr = {3.14, 1.23, 2.71, 0.99, 4.56};
    std::cout << "Original float array: ";
    for (const float &num : floatArr) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    bubbleSort(floatArr);

    std::cout << "Sorted float array: ";
    for (const float &num : floatArr) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
