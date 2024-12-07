n, m, k = map(int, input().split())
p = list(map(int, input().split()))
s = list(map(int, input().split()))
c = list(map(int, input().split()))

d = {p[i]: s[i] for i in range(n)}

ans = 0

for i in c:
  mx = 0
  for j in d:
    if d[j] == d[p[i - 1]] and j > p[i - 1]:
      mx = j
  
  if p[i - 1] < mx:
    ans += 1

print(ans)