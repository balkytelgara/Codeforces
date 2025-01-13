n = int(input())
a = list(map(int, input().split()))
anst, ans = 1000000, 10000000

for t in range(1, n + 1):
  temp = 0
  for i in range(n):
    if abs(a[i] - t) >= 1:
      temp += abs(a[i] - t) - 1

  if temp < ans:
    ans = temp
    anst = t

print(anst, ans)