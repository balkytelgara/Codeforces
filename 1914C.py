for _ in range(int(input())):
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  ans = s = mx = 0

  for i in range(min(n, k)):
    s += a[i]
    mx = max(mx, b[i])
    ans = max(ans, s + mx * (k - i - 1))

  print(ans)