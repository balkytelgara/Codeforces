n = int(input())
b = list(map(int, input().split()))
ans = 0
k = 0
for i in range(n):
  ans += abs(b[i] - k)
  k = k + (b[i] - k)

print(ans)