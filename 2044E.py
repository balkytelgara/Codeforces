def solve():
  k, l1, r1, l2, r2 = map(int, input().split())
  ans = 0
  for x in range(l1, r1 + 1):
    f = l2
    i = 1
    while f % x != 0:
      f += 1

    while k * f * i < r2:
      ans += 1
      i += 1
  print(ans)

for _ in range(int(input())):
  solve()