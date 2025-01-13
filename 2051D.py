from bisect import bisect_left
from bisect import bisect_right

def solve():
  n, x, y = map(int, input().split())
  a = sorted(map(int, input().split()))
  s = sum(a)
  ans = 0

  for i in range(n):
    mn = s - y - a[i]
    mx = s - x - a[i]
    if a[-1] < mn:
      continue

    if a[(i + 1 if i < n - 1 else n - 1)] > mx:
      continue

    j1 = bisect_left(a[i + 1:], mn) + i + 1
    j2 = bisect_right(a, mx)
    ans += j2 - j1

  print(ans)

for _ in range(int(input())):
  solve()