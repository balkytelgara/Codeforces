from math import gcd

for _ in range(int(input())):
  a, b = map(int, input().split())

  if b % a == 0:
    print(b ** 2 // a)
  else:
    print((a * b) // gcd(a, b))