n, k = map(int, input().split())
csize = 0

for _ in range(n):
  l, r = map(int, input().split())
  csize += r - l + 1

if csize % k:
  print(k - csize % k)
else:
  print(0)