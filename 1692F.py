COMBINATIONS = [
  (1, 5, 7), (1, 6, 6), (1, 3, 9), (1, 4, 8), (0, 6, 7),
  (6, 8, 9), (3, 5, 5), (0, 1, 2), (5, 9, 9), (2, 5, 6),
  (3, 4, 6), (0, 0, 3), (3, 3, 7), (2, 4, 7), (2, 3, 8),
  (0, 5, 8), (0, 4, 9), (2, 2, 9), (7, 8, 8), (4, 4, 5),
  (7, 7, 9), (1, 1, 1)
]

for _ in range(int(input())):
  n = int(input())
  a = list(map(lambda x: int(x) % 10, input().split()))
  f = {}
  for i in a:
    f[i] = f.get(i, 0) + 1

  for d1, d2, d3 in COMBINATIONS:
    if d1 == d2 or d2 == d3 or d1 == d3:
      if d1 == d2:
        if f.get(d1) and f.get(d1) > 1 and f.get(d3):
          print("YES")
          break
      elif d2 == d3:
        if f.get(d2) and f.get(d2) > 1 and f.get(d1):
          print("YES")
          break
      elif d1 == d3:
        if f.get(d1) and f.get(d1) > 1 and f.get(d2):
          print("YES")
          break
      else:
        if f.get(d1) and f.get(d1) > 2:
          print("YES")
          break
    else:
      if f.get(d1) and f.get(d2) and f.get(d3):
        print("YES")
        break
  else:
    print("NO")