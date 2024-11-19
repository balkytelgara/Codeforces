n, m = map(int, input().split())
a = sorted(map(int, input().split()))

best = a[n - 1] - a[0]

for i in range(1, m - n + 1):
  best = min(best, a[i + n - 1] - a[i])

print(best)
