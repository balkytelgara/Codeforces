from itertools import combinations

def solve():
  n = int(input())
  a = list(map(int, input().split()))

  for i in range(1, n):
    for comb in combinations([a[i], a[i - 1]] * 3, 3):
      x, y, z = comb

      if not (x + y > z and x + z > y and y + z > x):
        break
    else:
      print("YES")
      return

  print("NO")

for _ in range(int(input())): solve()