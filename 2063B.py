for _ in range(int(input())):
  n, l, r = map(int, input().split())
  a = sorted(map(int, input().split()))
  ans = 0
  
  for i in range(r - l + 1):
    ans += a.pop(0)

  print(ans)