for _ in range(int(input())):
  n, k = map(int, input().split())
  a = sorted(map(int, input().split()))
  ans = 0
  p = [0] * (n + 1)

  for i in range(n):
    p[i + 1] = p[i] + a[i]

  for m in range(k + 1):
    ans = max(ans, p[n - (k - m)] - p[2 * m])

  print(ans)