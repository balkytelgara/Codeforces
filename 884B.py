n, x = map(int, input().split())
a = sum(map(int, input().split()))

if a + (n - 1) == x:
  print("YES")
else:
  print("NO")