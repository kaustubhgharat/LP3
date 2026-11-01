#include <iostream>
using namespace std;

// Calculate Fibonacci numbers using an iterative approach
void fibonacciIterative(int n) {

    long long first = 0, second = 1;

    cout << "Fibonacci using non-recursive approach: ";
    for (int i = 0; i < n; i++) {
        cout << first << " "; 
        long long next = first + second;
        first = second;
        second = next;
    }

    cout<< endl;
}

// Calculate Fibonacci numbers using recursion
long long fibonacciRecursive(int n) {
    if (n <= 1) {
        return n;
    }

    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}

int main() {
    int n;

    cout << "Enter the value of n: ";
    cin >> n;

    if (n < 0 || n > 45) {
        cout << "Please enter n between 0 and 45 to avoid overflow and long execution time.\n";
        return 0;
    }

    fibonacciIterative(n);
    
    cout << "Fibonacci using recursive approach: ";
     for (int i = 0; i < n; i++) {
        cout << fibonacciRecursive(i) << " ";
    }
    return 0;
}

/*
Time Complexity:
1. Iterative: O(n)
2. Recursive: O(2^n) approximately

Space Complexity:
1. Iterative: O(1)
2. Recursive: O(n), due to the recursion stack
*/
