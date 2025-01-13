#include <iostream>
#include <stdio.h>
using namespace std;

#define ll long long

int main() {
  ll n, x;
  ll ans = 10000000;
  cin >> n;
  ll a[n];
  
  for (ll i = 0; i < n; i++) {
    cin >> a[i];
  }

  for (ll i = 1; i <= 100; i++) {
    ll tmp = 0;
    for (ll j = 0; j < n; j++) {
      ll d = abs(a[j] - i);
      if (d >= 1) {
        tmp += d - 1;
      }
    }

    if (tmp < ans) {
      ans = tmp;
      x = i;
    }
  }

  cout << x << " " << ans << endl;
  return 0;
}