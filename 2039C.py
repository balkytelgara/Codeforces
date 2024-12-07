for _ in range(int(input())):
  x, m = map(int, input().split())
  k = 0
  
  for i in range(1, m + 1):
    r = x | i
    if i != x and (x % r == 0 or i % r == 0):
      k += 1
  
  print(k)