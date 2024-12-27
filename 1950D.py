from math import log10

def bd(n):
  while n != 0:
    if n % 10 > 1:
      return False

    n //= 10

  return True

def solve():
  n = int(input())
  temp = n
  while temp != 0:
    if temp % 10 > 1:
      if n % 11 == 0:
        while n % 11 == 0:
          n //= 11

        if bd(n):
          return "YES"
      break
    temp //= 10
  else:
    return "YES"

  return "NO"

for _ in range(int(input())):
  print(solve())