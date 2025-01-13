for _ in range(int(input())):
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
  ans = 0
  f, s = k // 2 + k % 2, k // 2

  while f > 0 and n > 0:
    mn = min(a[0], f)
    a[0] -= mn
    f -= mn

    if a[0] == 0:
      a.pop(0)
      ans += 1
      n -= 1

  while s > 0 and n > 0:
    mn = min(a[-1], s)
    a[-1] -= mn
    s -= mn

    if a[-1] == 0:
      a.pop()
      ans += 1
      n -= 1

  print(ans)