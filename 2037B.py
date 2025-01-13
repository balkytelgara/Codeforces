from collections import defaultdict
from math import sqrt

def solve():
  n = int(input())
  a = list(map(int, input().split()))

  fmap = defaultdict(int)
  cmap = defaultdict(int)

  for i in a:
    fmap[i] = True
    cmap[i] = 1 if not cmap.get(i) else cmap[i] + 1

  for i in a:
    j = (n - 2) / i
    if fmap.get(j):
      if i != j:
        print(i, int(j))
        return
      else:
        if cmap[i] > 1:
          print(i, int(j))
          return

  print(1, n - 2)

for _ in range(int(input())): solve()