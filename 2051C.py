for _ in range(int(input())):
  n, m, k = map(int, input().split())
  a = list(map(int, input().split()))
  q = list(map(int, input().split()))
  u = [False for i in range(n + 1)]

  for i in q:
    u[i] = True

  if m == k:
    print("1" * m)
  elif k != n - 1:
    print("0" * m)
  else:
    for i in range(m):
      print(int(not u[a[i]]), end='')
    print()