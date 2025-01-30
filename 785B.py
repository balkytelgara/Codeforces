minr1 = minr2 = 10_000_000_000
maxl1 = maxl2 = 0

n = int(input())
for _ in range(n):
  l, r = map(int, input().split())
  minr1 = min(minr1, r)
  maxl1 = max(maxl1, l)

m = int(input())
for _ in range(m):
  l, r = map(int, input().split())
  minr2 = min(minr2, r)
  maxl2 = max(maxl2, l)

print(max(0, max(maxl2 - minr1, maxl1 - minr2)))