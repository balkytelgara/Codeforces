from math import (
  sqrt,
  floor
)

for _ in range(int(input())):
  a, b = map(int, input().split())
  p = a + b

  if a - b == 1:
    for i in range(2, floor(sqrt(p)) + 1):
      if p % i == 0:
        print("NO")
        break
    else:
      print("YES")
  else:
    print("NO")