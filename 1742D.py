from math import gcd

for _ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))
  ans = -1
  b = {}

  for i in range(n):
    b[a[i]] = i + 1

  for i in b.keys():
    for j in b.keys():
      if gcd(i, j) == 1:
        ans = max(ans, b[i] + b[j])

  print(ans)