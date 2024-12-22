n, n1, n2 = map(int, input().split())
a = sorted(map(int, input().split()))

n1, n2 = min(n1, n2), max(n1, n2)

f = 0
s = 0

for i in range(n - n1, n):
  f += a[i]

for i in range(n - n1 - n2, n - n1):
  s += a[i]

print(f / n1 + s / n2)