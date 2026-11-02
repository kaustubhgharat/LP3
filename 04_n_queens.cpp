#include <bits/stdc++.h>
using namespace std;

// Check whether a queen can be placed at board[row][col]
bool isSafe(const vector<vector<int>>& board, int row, int col, int n) {
    // Check the same column in previous rows
    for (int i = 0; i < row; i++) {
        if (board[i][col] == 1) {
            return false;
        }
    }

    // Check the upper-left diagonal
    for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
        if (board[i][j] == 1) {
            return false;
        }
    }

    // Check the upper-right diagonal
    for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
        if (board[i][j] == 1) {
            return false;
        }
    }

    return true;
}

// Place queens row by row using backtracking
bool solveNQueens(vector<vector<int>>& board, int row, int n) {
    if (row == n) {
        return true;
    }

    for (int col = 0; col < n; col++) {
        if (isSafe(board, row, col, n)) {
            board[row][col] = 1;

            if (solveNQueens(board, row + 1, n)) {
                return true;
            }

            // Undo the placement and try the next column
            board[row][col] = 0;
        }
    }

    return false;
}

int main() {
    int n;

    cout << "Enter value of N: ";
    cin >> n;

    if (n <= 0) {
        cout << "N must be positive.\n";
        return 0;
    }

    vector<vector<int>> board(n, vector<int>(n, 0));

    // Place the first queen before solving the remaining rows
    board[0][0] = 1;

    if (solveNQueens(board, 0, n)) {
        cout << "\nSolution (Q = Queen, . = Empty):\n";
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cout << (board[i][j] ? "Q " : ". ");
            }
            cout << endl;
        }
    } else {
        cout << "No solution exists with the first queen in that column.\n";
    }

    return 0;
}

/*
Time Complexity: O(N!), in the worst case.
Space Complexity: O(N^2) for the board, plus O(N) recursion stack.
*/
