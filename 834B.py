n, k = map(int, input().split())
s: str = input()

last: dict = {}
for i in range(n):
  last[s[i]] = i

active: dict = {}
for i in range(n):
  active[s[i]] = 0

  if len(active) > k:
    print("YES")
    break

  if last[s[i]] == i:
    del active[s[i]]
else:
  print("NO")