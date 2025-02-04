from math import (
  log10,
  floor
)

def digitsum(n: int) -> int:
  res = 0
  while n:
    res += n % 10
    n //= 10
  return res

n = int(input())
logn = floor(log10(n))
ans = 0
if n <= 10:
  print(n)
else:
  for i in range(logn):
    ans += 9 * pow(10, i)
  ans += (int(str(n)[0]) - 1) * pow(10, logn)

  print(digitsum(ans) + digitsum(n - ans))