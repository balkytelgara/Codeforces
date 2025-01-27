for _ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))

  for i in range(n):
    if 2 * (n - (i + 1)) >= a[i] or 2 * i >= a[i]:
      print("NO")
      break
  else:
    print("YES")