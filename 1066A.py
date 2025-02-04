from math import ceil

for _ in range(int(input())):
  L, u, l, r = map(int, input().split())

  total = L // u
  print(total - (r // u - (l - 1) // u))