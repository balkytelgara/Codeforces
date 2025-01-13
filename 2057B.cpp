#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

void handleTest() {
    int n, k;
    cin >> n >> k;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    
    int ans = 0;
    map<int, int> freqmap;

    for (int i : a) {
        freqmap[i]++;
    }

    vector<int> b;
    for (const auto& pair : freqmap) {
        b.push_back(pair.second);
    }
    
    sort(b.begin(), b.end());
    int m = b.size();
    for (int i = 0; i < m - 1; ++i) {
        if (b[i] > k) {
            cout << m - i << endl;
            return;
        }
        k -= b[i];
    }
    cout << 1 << endl;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        handleTest();
    }
    return 0;
}

