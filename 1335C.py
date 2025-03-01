for _ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))
  f = {}

  for i in range(n):
    f[a[i]] = f.get(a[i], 0) + 1

  k = list(f.keys())
  v = list(f.values())

  mx = max(v)
  for i in k:
    if f[i] == mx:
      need = i
      break

  first = len(k) - 1
  second = f[need]

  if second <= first:
    print(second)
  else:
    if second - first >= 2:
      print(first + 1)
    else:
      print(first)
