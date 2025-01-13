#include <iostream>
#include <map>
#include <vector>

using namespace std;

void solve() {
  int n;
  cin >> n;

  int a[n], b[n];
  map<int, bool> seen;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    seen[a[i]] = true;
  }

  map<int, bool> freq;
  vector<int> use;

  for (int i = 1; i <= n; i++) {
    if (seen.find(i) == seen.end()) {
      use.push_back(i);
    }
  }
  int k = 0;
  for (int i = 0; i < n; i++) {
    if (freq.find(a[i]) == freq.end()) {
      b[i] = a[i];
      freq[a[i]] = true;
    } else {
      b[i] = use[k];
      k++;
    }
  }

  for (int i = 0; i < n; i++) {
    cout << b[i] << " ";
  }

  cout << endl;
}

int main() {
  int T;
  cin >> T;
  while (T--) {
    solve();
  }

  return 0;
}