n = int(input())
a = list(map(int, input().split()))
e, o = [], []

for i in range(n):
  if a[i] % 2 == 0:
    e.append(a[i])
  else:
    o.append(a[i])

if len(e) < len(o):
  print(a.index(e[0]) + 1)
else:
  print(a.index(o[0]) + 1)