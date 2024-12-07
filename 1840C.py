for _ in range(int(input())):
  n, k, q = map(int, input().split())
  a = [1 if i <= q else 0 for i in list(map(int, input().split()))]
  
  ans = 0
  l = 0
  for i in range(n):
    if a[i] == 1:
      l += 1
    else:
      if l >= k:
        ans += (l - k + 1) * (l - k + 2) // 2
      l = 0
  
  if l >= k:
    ans += (l - k + 1) * (l - k + 2) // 2
  
  print(ans)