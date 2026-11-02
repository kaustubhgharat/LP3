#include <bits/stdc++.h>
using namespace std;


struct Node {
    char ch;
    int freq;
    Node *left, *right;

    Node(char c, int f) {
        ch = c;
        freq = f;
        left = right = nullptr;
    }
};

// The priority queue keeps the node with minimum freq at the top
struct Compare {
    bool operator()(Node* a, Node* b) {
        return a->freq > b->freq;
    }
};

// Print the Huffman code of each character
void printCodes(Node* root, string code) {
    if (root == nullptr) {
        return;
    }

    // A leaf node represents an input character
    if (root->left == nullptr && root->right == nullptr) {
        cout << root->ch << " : " << (code.empty() ? "0" : code) << endl;
        return;
    }

    printCodes(root->left, code + "0");
    printCodes(root->right, code + "1");
}

int main() {
    int n;
    char ch;
    int freq;

    cout << "Enter number of characters: ";
    cin >> n;

    if (n <= 0) {
        cout << "Number of characters must be positive.\n";
        return 0;
    }
    
    priority_queue<Node*, vector<Node*>, Compare> minHeap;

    cout << "Enter each character and its freq:\n";
    for (int i = 0; i < n; i++) {
        cin >> ch >> freq;

        if (freq < 0) {
            cout << "freq cannot be negative.\n";
            return 0;
        }

        minHeap.push(new Node(ch, freq));
    }

    // Repeatedly combine the two nodes with the lowest frequencies
    while (minHeap.size() > 1) {
        Node* left = minHeap.top();
        minHeap.pop();

        Node* right = minHeap.top();
        minHeap.pop();

        Node* parent = new Node('$', left->freq + right->freq);
        parent->left = left;
        parent->right = right;

        minHeap.push(parent);
    }

    cout << "\nHuffman Codes:\n";
    printCodes(minHeap.top(), "");

    return 0;
}

/*
a 50
b 25
c 15
d 10
Time Complexity: O(n log n), where n is the number of characters.
Space Complexity: O(n), for the Huffman tree and priority queue.
*/
