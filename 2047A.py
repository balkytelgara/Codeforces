for _ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))
  s = sum(a)

  k = 1
  ans = 0

  while s - (k ** 2) >= 0:
    ans += 1
    k += 2
  
  print(ans)