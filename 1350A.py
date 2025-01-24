from math import sqrt

for _ in range(int(input())):
  n, k = map(int, input().split())

  d = n
  for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0:
      d = i
      break

  print(n + d + (k - 1) * 2)