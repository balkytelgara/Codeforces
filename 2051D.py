for _ in range(int(input())):
  n, x, y = map(int, input().split())
  a = list(map(int, input().split()))
  s = sum(a)
  ans = 0

  for i in range(n):
    for j in range(i + 1, n):
      d = s - (a[i] + a[j])
      if d >= x and d <= y:
        ans += 1

  print(ans)