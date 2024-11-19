for _ in range(int(input())):
  n, m, r, c = map(int, input().split())
  print(m * (n - r) + n * m - ((r - 1) * m + c) - (n - r))
