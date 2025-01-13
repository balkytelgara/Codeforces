n = int(input())
l = [0] * n
r = [0] * n

for _ in range(n):
  L, R = map(int, input().split())
  l[_] = L
  r[_] = R

sl = sum(l)
sr = sum(r)
ans = abs(sl - sr)
index = 0

for i in range(n):
  L, R = l[i], r[i]

  tsl = sl - L + R
  tsr = sr - R + L

  if abs(tsl - tsr) > ans:
    ans = abs(tsl - tsr)
    index = i + 1

print(index)