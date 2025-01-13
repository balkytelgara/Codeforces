n = int(input())
a = list(map(int, input().split()))
m = max(a)
ans = 0
c = 0

for i in a:
  if i == m:
    c += 1
  else:
    ans = max(ans, c)
    c = 0

print(max(ans, c))