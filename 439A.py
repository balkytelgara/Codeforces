n, d = map(int, input().split())
t = list(map(int, input().split()))
k = (n - 1) * 10

if sum(t) + k > d:
  print(-1)
else:
  print(k // 5 + (d - (k + sum(t))) // 5)