from math import ceil

for _ in range(int(input())):
  n, k, p = map(int, input().split())

  ans = ceil(abs(k) / p)

  if ans > n:
    print(-1)
  else:
    print(ans)