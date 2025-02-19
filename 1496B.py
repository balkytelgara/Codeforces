from math import ceil

for _ in range(int(input())):
  n, k = map(int, input().split())
  a = sorted(map(int, input().split()))
  max = a[-1]
  freq = {}

  for i in range(n):
    if not freq.get(i):
      freq[i] = 1

  if k == 0:
    print(len(freq.keys()))
    continue

  if a[0] != 0:
    mex = 0
  else:
    for i in range(n - 1):
      if a[i + 1] - a[i] > 1:
        mex = a[i] + 1
        break
    else:
      print(len(freq.keys()) + k)
      continue

  if freq.get(ceil((mex + max) / 2)):
    print(len(freq.keys()))
  else:
    print(len(freq.keys()) + 1)