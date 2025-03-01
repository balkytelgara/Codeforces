from math import gcd

for _ in range(int(input())):
  n = int(input())
  a = sorted(map(int, input().split()))
  d = []

  for i in range(n - 1):
    d.append(a[i + 1] - a[i])

  ans = gcd(*d)

  if ans == 0:
    print(-1)
  else:
    print(ans)