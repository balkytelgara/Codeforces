for _ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))
  p = [0] * n
  f = {}
  mex = 0
  for i in range(n):
    if a[i] >= 0:
      p[i] = mex
    else:
      p[i] = mex - a[i]

    f[p[i]] = True
    while f.get(mex, False):
      mex += 1

  print(*p)