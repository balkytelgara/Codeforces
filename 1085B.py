n, k = map(int, input().split())
ans = 0
for i in range(1, k):
  if n % i == 0:
    ans = k * (n // i) + i

print(ans)