for _ in range(int(input())):
  n, m = map(int, input().split())
  ans = 4 * m
  
  _x, _y = map(int, input().split())
  for _ in range(n - 1):
    x, y = map(int, input().split())
    ans += x * 2
    ans += y * 2
    
  print(ans)