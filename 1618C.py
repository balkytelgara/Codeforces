from math import gcd

for _ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))
  even = []
  odd = []

  for i in range(n):
    if i % 2 == 0:
      even.append(a[i])
    else:
      odd.append(a[i])

  egcd = gcd(*even)
  ogcd = gcd(*odd)

  b = a.copy()
  c = a.copy()

  for i in range(n):
    b[i] = b[i] % egcd == 0

  for i in range(n - 1):
    if b[i] == b[i + 1]:
      break
  else:
    print(egcd)
    continue

  for i in range(n):
    c[i] = c[i] % ogcd == 0

  for i in range(n - 1):
    if c[i] == c[i + 1]:
      print(0)
      break
  else:
    print(ogcd)