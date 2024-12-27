#include <iostream>

using namespace std;

int main() {
  long long a, b;
  int ans;

  cin >> a >> b;

  if (a - b >= 10)
    cout << 0 << endl;
  else {
    ans = 1;
    for (long long i = a + 1; i <= b; i++)
      ans = (1LL * ans * (i % 10)) % 10;
    
    cout << ans << endl;
  }

  return 0;
}