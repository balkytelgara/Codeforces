k = int(input())
n = map(int, list(input()))
n = sorted(n)

c = sum(n)
ans = 0

for i in n:
  if c < k:
    c += 9 - i
    ans += 1

print(ans) 