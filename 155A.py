n = int(input())
a = list(map(int, input().split()))
ans = 0
mx = a[0]
mn = a[0]

for i in range(1, n):
  if a[i] > mx or a[i] < mn:
    mx = max(mx, a[i])
    mn = min(mn, a[i])
    ans += 1
 
print(ans)