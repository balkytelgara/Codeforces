n = int(input())
a = sorted(map(int, input().split()))

if a[-1] >= a[-2] + a[-3]:
  print("NO")
else:
  print("YES")
  for i in range(n - 1, -1, -2):
    print(a[i], end=" ")

  for i in range(n % 2, n, 2):
    print(a[i], end=" ")