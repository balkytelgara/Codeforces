from math import ceil

for _ in range(int(input())):
  a, b, c, d = map(int, input().split())

  if b >= a:
    print(b)
  elif d >= c:
    print(-1)
  else:
    x = ceil((a - b) / (c - d))

    print(b + x * c)