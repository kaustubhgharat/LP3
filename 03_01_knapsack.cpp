#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, capacity;

    cout << "Enter number of items: ";
    cin >> n;
    cout << "Enter knapsack capacity: ";
    cin >> capacity;

    if (n <= 0 || capacity < 0) {
        cout << "Please enter a positive number of items and non-negative capacity.\n";
        return 0;
    }

    vector<int> weights(n), values(n);

    cout << "Enter weights of items:\n";
    for (int i = 0; i < n; i++) {
        cin >> weights[i];
        if (weights[i] < 0) {
            cout << "Weights cannot be negative.\n";
            return 0;
        }
    }

    cout << "Enter values of items:\n";
    for (int i = 0; i < n; i++) {
        cin >> values[i];
    }

    // dp[i][w] stores the maximum value using the first i items
    // when the available capacity is w
    vector<vector<int>> dp(n + 1, vector<int>(capacity + 1, 0));

    for (int i = 1; i <= n; i++) {
        for (int w = 0; w <= capacity; w++) {
            // Option 1: do not include the current item
            dp[i][w] = dp[i - 1][w];

            // Option 2: include the current item if it fits
            if (weights[i - 1] <= w) {
                dp[i][w] = max(
                    dp[i][w],
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]
                );
            }
        }
    }

    cout << "\nMaximum value: " << dp[n][capacity] << endl;

    return 0;
}

/*
Enter number of items: 3

Enter weights of items:
10 20 30

Enter profits of items:
60 100 120

Enter knapsack capacity: 50

Time Complexity: O(n * capacity)
Space Complexity: O(n * capacity)
*/
