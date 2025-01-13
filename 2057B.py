from bisect import bisect_right
from math import ceil

for _ in range(int(input())):
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
  ans = 0
  freqmap = {}
 
  for i in a:
    freqmap[i] = freqmap.get(i, 0) + 1
 
  b = sorted(freqmap.values())
  m = len(b)
  for i in range(m - 1):
    if b[i] > k:
      print(m - i)
      break

    k -= b[i]
  else:
    print(1)