for _ in range(int(input())):
  n = int(input())

  l = 0
  r = min(2 * pow(10, 9), 2 * n)
  while r - l > 1:
    m = (l + r) >> 1

    if m * (m - 1) // 2 + m < n:
      l = m
    else:
      r = m

  y = n - r * (r - 1) // 2

  if ((r + 1) * r // 2 <= n):
    print(min(r + y, y + 1 + n - (r + 1) * r // 2))
  else:
    print(r + y)