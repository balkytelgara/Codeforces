#include <bits/stdc++.h>

using namespace std;

int main() {
  int n;
  cin >> n;

  vector<int> pos(n);

  for (int i = 0; i < n; i++) {
    cin >> pos[i];
  }

  int ans = 1e7;

  for (int i = 0; i < n; i++) {
    int curr = 0;
    if (i) curr = max(curr, pos[i - 1] - 1);
    if (i != n) curr = max(curr, 1000000 - pos[i]);

    ans = min(ans, curr);
  }

  cout << ans << endl;
}