for _ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))

  m, s = 0, 0

  for i in range(n - 1):
    if a[i] > b[i + 1]:
      m += a[i]
      s += b[i + 1]

  m += a[n - 1]

  print(m - s)