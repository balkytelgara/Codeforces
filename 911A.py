n = int(input())
a = list(map(int, input().split()))

mn = min(a)
l = []
ans = 10_000_000_000

for i in range(n):
  if a[i] == mn:
    l.append(i)

for i in range(len(l) - 1):
  ans = min(ans, l[i + 1] - l[i])

print(ans)