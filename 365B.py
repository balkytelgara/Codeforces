def solve():
  n = int(input())
  a = list(map(int, input().split()))
  ans = 0
  k = 0

  if n <= 2:
    print(n)
    return

  for i in range(2, n):
    if a[i - 1] + a[i - 2] == a[i]:
      k += 1
    else:
      ans = max(ans, k)
      k = 0
  else:
    ans = max(ans, k)

  print(ans + 2)

solve()