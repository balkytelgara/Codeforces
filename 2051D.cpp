#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve() {
  int n;
  long long x, y;
  cin >> n >> x >> y;
  long long ans = 0, s = 0;

  vector<long long> a(n);
  for (long long i = 0; i < n; ++i) {
    cin >> a[i];
    s += a[i];
  }

  sort(a.begin(), a.end());

  for (int i = 0; i < n; ++i) {
    long long mn = s - y - a[i];
    long long mx = s - x - a[i];
    if (a.back() < mn) {
        continue;
    }

    if (a[min(i + 1, n - 1)] > mx) {
        continue;
    }

    int j1 = lower_bound(a.begin() + i + 1, a.end(), mn) - a.begin();
    int j2 = upper_bound(a.begin(), a.end(), mx) - a.begin();
    ans += j2 - j1;
  }

  cout << ans << endl;
}

int main() {
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}