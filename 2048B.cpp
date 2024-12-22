#include <iostream>

using namespace std;

void solve() {
  int n, k;
  cin >> n >> k;

  int p[n];

  for (int i = n / k; i > 0; i--) {
    p[i * k - 1] = i;
  }

  int temp = n;
  for (int i = 0; i < n; i++) {
    if ((i + 1) % k != 0) {
      p[i] = temp--;
    }
  }

  for (int i = 0; i < n; i++) {
    cout << p[i] << " ";
  }

  cout << endl;
}

int main() {
  int t;
  cin >> t;
  while (t--) solve();
}