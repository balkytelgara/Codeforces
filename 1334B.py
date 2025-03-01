for _ in range(int(input())):
  n, x = map(int, input().split())
  a = sorted(map(int, input().split()))
  ans = 0
  s = 0

  for i in range(n - 1, -1, -1):
    s += a[i]
    if s / (n - i) < x:
      break
    else:
      ans += 1

  print(ans)