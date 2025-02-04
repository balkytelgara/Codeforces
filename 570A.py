n, m = map(int, input().split())
f = {}

for _ in range(m):
  vote = list(map(int, input().split()))
  mx = max(vote)

  for i in range(n):
    if vote[i] == mx:
      f[i + 1] = f.get(i + 1, 0) + 1
      break

mx = max(f.values())
for key in sorted(f.keys()):
  if f[key] == mx:
    print(key)
    break
