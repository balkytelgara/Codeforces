n = int(input())
a = list(map(int, input().split()))

ans = 0

lpos, rpos = 1, 1e6 - 1
l, r = 0, n - 1

while l <= r:
  if abs(a[l] - lpos) < abs(a[r] - rpos):
    ans += abs(a[l] - lpos)
    lpos = a[l]
    l += 1
  else:
    ans += abs(a[r] - rpos)
    rpos = a[r]
    r -= 1

print(int(ans))