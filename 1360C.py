for _ in range(int(input())):
  n = int(input())
  a = sorted(map(int, input().split()))
  even, odd = 0, 0

  for i in range(n):
    if a[i] % 2 == 0:
      even += 1
    else:
      odd += 1

  if even % 2 + odd % 2 == 0:
    print("YES")
  else:
    for i in range(n - 1):
      if a[i + 1] - a[i] == 1:
        print("YES")
        break
    else:
      print("NO")