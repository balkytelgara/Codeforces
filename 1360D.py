from math import (
  sqrt, ceil
)

for _ in range(int(input())):
  n, k = map(int, input().split())
  ans = 1e10

  for i in range(1, ceil(sqrt(n)) + 1):
    if n % i == 0:
      if i <= k:
        ans = min(ans, n // i)
      if n // i <= k:
        ans = min(ans, i)

  print(ans)