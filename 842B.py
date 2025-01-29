from math import sqrt

R, D = map(int, input().split())
n = int(input())
ans = 0

for _ in range(n):
  x, y, r = map(int, input().split())

  ans += (sqrt(x ** 2 + y ** 2) + r <= R) and \
         (sqrt(x ** 2 + y ** 2) >= R - D + r)

print(ans)