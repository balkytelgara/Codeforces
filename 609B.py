n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = {}

for i in a:
  cnt[i] = cnt.get(i, 0) + 1

bad = 0
for i in cnt:
  bad += cnt[i] * (cnt[i] - 1) // 2

print(n * (n - 1) // 2 - bad)