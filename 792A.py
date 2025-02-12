n = int(input())
a = sorted(map(int, input().split()))
mind = 1e10
ans = 0

for i in range(n - 1):
  mind = min(mind, abs(a[i] - a[i + 1]))

for i in range(n - 1):
  if abs(a[i] - a[i + 1]) == mind:
    ans += 1

print(mind, ans)