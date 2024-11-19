n, m, k = map(int, input().split())
a = sorted(map(int, input().split()))
ans = 0

while m > k:
  if len(a) > 0:
    m -= a.pop()
    k -= 1
    ans += 1
  else:
    print(-1)
    break
else:
  print(ans)