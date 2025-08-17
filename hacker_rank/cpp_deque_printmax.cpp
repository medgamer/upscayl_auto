#include <iostream>
#include <deque>
#include <algorithm> // For std::max_element if needed for a different approach

void printKMax(int arr[], int n, int k) {
    std::deque<int> Qi; // Stores indices of elements

    // Process first k elements (first window)
    for (int i = 0; i < k; ++i) {
        while ((!Qi.empty()) && arr[i] >= arr[Qi.back()]) {
            Qi.pop_back();
        }
        Qi.push_back(i);
    }

    // Process rest of the elements (remaining windows)
    for (int i = k; i < n; ++i) {
        std::cout << arr[Qi.front()] << " "; // Print max of previous window

        // Remove elements out of current window
        while ((!Qi.empty()) && Qi.front() <= i - k) {
            Qi.pop_front();
        }

        // Remove smaller elements from back and add current element
        while ((!Qi.empty()) && arr[i] >= arr[Qi.back()]) {
            Qi.pop_back();
        }
        Qi.push_back(i);
    }

    // Print max of the last window
    std::cout << arr[Qi.front()] << std::endl;
}

int main() {
    int t;
    std::cin >> t;
    while (t--) {
        int n, k;
        std::cin >> n >> k;
        int arr[n]; // C-style array for simplicity, std::vector is preferred in modern C++
        for (int i = 0; i < n; i++) {
            std::cin >> arr[i];
        }
        printKMax(arr, n, k);
    }
    return 0;
}
