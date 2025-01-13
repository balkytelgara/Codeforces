for _ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))
  b = [0] * n

  freq = {}

  r = {_: True for _ in a}
  s = [_ for _ in range(1, n + 1) if not r.get(_)]

  for i in range(n):
    if not freq.get(a[i]):
      b[i] = a[i]
      freq[a[i]] = True
    else:
      b[i] = s.pop()

  print(*b)