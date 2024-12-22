for _ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))

  i = 0
  ans = 0
  while i < n - 1:
    if a[i] == a[i + 1]:
      ans += 1
      i += 2
    i += 1

  print(ans)