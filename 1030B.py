n, d = map(int, input().split())
m = int(input())

for _ in range(m):
  x, y = map(int, input().split())

  if (d <= x + y and x + y <= 2 * n - d) and \
     (-d <= x - y and x - y <= d):
    print("YES")
  else:
    print("NO")