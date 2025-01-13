for _ in range(int(input())):
  n, m = map(int, input().split())
  print(max(1 + m, 1 + n))