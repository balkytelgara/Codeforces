from math import ceil

n = int(input())
s = map(int, input().split())
f = {1: 0, 2: 0, 3: 0}
ans = 0

for i in s:
  if i == 4:
    ans += 1
  else:
    f[i] += 1

if f.get(2):
  ans += f[2] // 2
  f[2] = f[2] % 2

m = min(f[1], f[3])
ans += m
f[1] -= m
f[3] -= m

if f[3]:
  ans += f[3] + f[2]
else:
  if not f[2]:
    ans += ceil(f[1] / 4)
  else:
    ans += f[2]
    ans += ceil((f[1] - min(f[1], 2)) / 4)

print(ans)