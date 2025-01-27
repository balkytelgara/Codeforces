from math import (
  sqrt,
  ceil,
  floor
)

n = int(input())
a = int(ceil(sqrt(n)))
b = int(floor(sqrt(n)))

print(a + b + (not a * b >= n))