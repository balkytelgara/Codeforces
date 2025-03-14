n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
f = {}
v, p = 0, 0

for i in range(n):
  f[a[i]] = i + 1

for i in range(m):
  v += f[b[i]]
  p += n - f[b[i]] + 1

print(v, p)