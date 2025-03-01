from math import ceil

def cbrt(n: int) -> int:
  return ceil(n ** (1 / 3))

for _ in range(int(input())):
  x = int(input())
  if x == 1:
    print("NO")
    continue

  for a in range(1, cbrt(x)):
    b = cbrt(x - (a ** 3))
    if a ** 3 + b ** 3 == x:
      print("YES")
      break
  else:
    print("NO")