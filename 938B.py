n = int(input())
a = [1] + list(map(int, input().split())) + [pow(10, 6)]

ans = pow(10, 6)
l, r = 0, n + 1

while n > 0:
  if abs(a[l] - a[l + 1]) <= abs(a[r] - a[r - 1]):
    ans = min(ans, abs(a[l] - a[l + 1]))
    l += 1
  else:
    ans = min(ans, abs(a[r] - a[r - 1]))
    r -= 1

  n -= 1

print(ans)