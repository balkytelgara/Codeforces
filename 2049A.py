for _ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))

  ans = 0
  k = 0
  for i in a:
    if i > 0:
      k += 1
    else:
      if k > 0:
        ans += 1
      k = 0
  else:
    if k > 0:
      ans += 1
      
  print(ans)