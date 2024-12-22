n = int(input())
a, b = set(), set()

for _ in range(n):
  x, y = map(int, input().split())
  a.add(x)
  b.add(y)

if len(a) != 2 or len(b) != 2:
  print(-1)
else:
  a = list(a)
  b = list(b)

  print(abs(a[0] - a[1]) * abs(b[0] - b[1]))