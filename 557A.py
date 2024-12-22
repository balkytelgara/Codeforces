n = int(input())
min1, max1 = map(int, input().split())
min2, max2 = map(int, input().split())
min3, max3 = map(int, input().split())

if max1 + min2 + min3 <= n:
  print(n - min2 - min3, min2, min3)
elif max1 + max2 + min3 <= n:
  print(max1, n - max1 - min3, min3)
else:
  print(max1, max2, n - max1 - max2)