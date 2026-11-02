#include <bits/stdc++.h>
using namespace std;

long long comparisons = 0;

// Partition function
int partition(vector<int> &a, int low, int high) {
    int pivot = a[high];
    int i = low - 1;
    comparisons++;
    for (int j = low; j < high; j++) {
        if (a[j] <= pivot) {
            i++;
            swap(a[i], a[j]);
        }
    }

    swap(a[i + 1], a[high]);
    return i + 1;
}

// Deterministic Quick Sort
void quickSort(vector<int> &a, int low, int high) {
    if (low < high) {
        int p = partition(a, low, high);

        quickSort(a, low, p - 1);
        quickSort(a, p + 1, high);
    }
}

// Randomized Quick Sort
void randomizedQuickSort(vector<int> &a, int low, int high) {
    if (low < high) {

        // Select random pivot
        int random = low + rand() % (high - low + 1);

        swap(a[random], a[high]);

        int p = partition(a, low, high);

        randomizedQuickSort(a, low, p - 1);
        randomizedQuickSort(a, p + 1, high);
    }
}

// Display array
void display(vector<int> &a, int n) {
    for (int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }
    cout << endl;
}

int main() {
    int n;
    cout << "Enter number of elements: ";
    cin >> n;

    vector<int> a(n),b(n);
    cout << "Enter array elements:\n";
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        b[i] = a[i];
    }

    srand(time(0));// Initialize random number generator


    comparisons = 0;
    quickSort(a, 0, n - 1);
    long long deterministicComparisons = comparisons;

    cout << "\nDeterministic Quick Sort: ";
    display(a, n);
    cout << "\nDeterministic Quick Sort Comparisons: " << deterministicComparisons << endl;

    comparisons = 0;
    randomizedQuickSort(b, 0, n - 1);
    long long randomizedComparisons = comparisons;

    cout << "Randomized Quick Sort: ";
    display(b, n);
    cout << "Randomized Quick Sort Comparisons: " << randomizedComparisons << endl;

    return 0;
}

/*
Time Complexity:
1. Best/Average: O(n log n)
2. Worst: O(n^2)

Deterministic Quick Sort uses a fixed pivot rule, so particular input orders
can produce poor partitions. Randomized Quick Sort chooses a random pivot,
making consistently poor partitions less likely.

Space Complexity:
Average: O(log n) recursion stack
Worst: O(n) recursion stack
*/
