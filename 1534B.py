n = int(input())
a = sorted(map(int, input().split()))

mx = 0

for i in range(1, n - 1):
  mx = max((a[0] - a[i]) * (a[i] - a[-1]), mx)

print(mx)