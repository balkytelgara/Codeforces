#include <iostream>
#include <vector>

using namespace std;

void solve() {
  long long n, ans = 0;
  long long k;

  cin >> n >> k;
  
  vector<long long> a(n);
  for (long long i = 0; i < n; i++) {
    cin >> a[i];
  }

  long long f = n / 2 + n % 2, s = n / 2;
  while (f > 0 && n > 0) {
    long long mn = min(a[0], f);
    a[0] -= mn;
    f -= mn;

    if (a[0] == 0) {
      a.erase(a.begin());
      n--;
      ans++;
    }
  }

  while (s > 0 && n > 0) {
    long long mn = min(a.back(), s);
    a.back() -= mn;
    s -= mn;

    if (a.back() == 0) {
      a.pop_back();
      n--;
      ans++;
    }
  }

  cout << ans << endl;
}

int main() {
  long long T;
  cin >> T;
  while (T--) {
    solve();
  }

  return 0;
}