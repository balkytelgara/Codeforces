n = int(input())
p = []
h = []
b = []
W = 0

for _ in range(n):
  wi, hi = map(int, input().split())
  W += wi
  p.append((wi, hi))
  h.append(hi)

h.sort()

for wi, hi in p:
  if h[-1] == hi:
    b.append((W - wi) * h[-2])
  else:
    b.append((W - wi) * h[-1])

print(*b)