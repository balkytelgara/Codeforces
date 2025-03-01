n = int(input())
a = list(map(int, input().split()))
p = [1 << i for i in range(1, 31)]
f = {}
s = {}
ans = 0

for i in range(n):
  f[a[i]] = f.get(a[i], 0) + 1

for i in range(n):
  for power in p:
    if a[i] <= power:
      j = power - a[i]
      o = tuple(sorted((i, j)))

      if a[i] != j and f.get(j) and not s.get(o):
        s[o] = 1
        ans += 1
      elif a[i] == j and f.get(j) > 1 and not s.get(o):
        s[o] = 1
        ans += 1

print(ans)