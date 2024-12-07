for _ in range(int(input())):
  n = int(input())
  s = []
  i = 0
 
  for j in range(1, n + 1):
    s.append(j + i)
    i += 1
  
  print(*s)