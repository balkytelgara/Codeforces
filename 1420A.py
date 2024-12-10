for _ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))

  for i in range(1, n):
    if a[i] >= a[i - 1]:
      print("YES")
      break
  else:
    print("NO")