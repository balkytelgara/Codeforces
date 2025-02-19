n: int = int(input())
d: dict = {}
minl: float = 1e10
maxr: int = 0

for _ in range(n):
  l, r = map(int, input().split())
  d[(l, r)] = _ + 1

  minl = min(minl, l)
  maxr = max(maxr, r)

print(d.get((minl, maxr), -1))