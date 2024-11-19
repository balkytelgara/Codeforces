for _ in range(int(input())):
  n, x = map(int, input().split())
  a = list(map(int, input().split()))
  s, m = 0, 0

  for i in a:
    s += i
    m = max(m, i)

  print(max(m, (s + x - 1) // x))
