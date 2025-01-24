n, t, c = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
L = 0

for i in range(n):
  if a[i] <= t:
    L += 1
  else:
    if L >= c:
      ans += L - c + 1

    L = 0

if L >= c:
  ans += L - c + 1

print(ans)