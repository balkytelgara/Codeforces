#include <iostream>
#include <map>

using namespace std;

void solve() {
  map<int, int> counter;
  map<int, bool> freqmap;
  int n;
  cin >> n;

  int a[n];
  for (int i = 0; i < n; i++) {
    cin >> a[i];

    if (counter.find(a[i]) == counter.end()) {
      counter[a[i]] = 1;
    } else {
      counter[a[i]] += 1;
    }

    freqmap[a[i]] = true;
  }

  for (int i = 0; i < n; i++) {
    int j = (n - 2) / a[i];
    if (a[i] * j == n - 2 && freqmap.find(j) != freqmap.end()) {
      if (a[i] != j) {
        cout << a[i] << ' ' << j << endl;
        return;
      } else {
        if (counter[a[i]] > 1) {
          cout << a[i] << ' ' << j << endl;
          return;
        }
      }
    }
  }

  cout << 1 << ' ' << n - 2 << endl;
}

int main() {
  int t;
  cin >> t;
  while (t--) {
    solve();
  }

  return 0;
}