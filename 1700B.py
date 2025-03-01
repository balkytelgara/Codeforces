def ispalindrome(n: int) -> bool:
  return str(n) == str(n)[::-1]

for _ in range(int(input())):
  n = int(input())
  s = int(input())
  t = s + 1
  while not ispalindrome(t):
    t += 1
  else:
    print(t - s)