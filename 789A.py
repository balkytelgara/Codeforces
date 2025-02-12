from math import ceil

n, k = map(int, input().split())
w = list(map(int, input().split()))
ans = 0

for i in range(n):
  ans += ceil(w[i] / k)

print(ceil(ans / 2))