for _ in range(int(input())):
  n, k = map(int, input().split())
  a = list(map(int, input().split()))

  ans = 1e9
  for j in range(1, max(a) + 1):
    count = 0
    i = 0
    while i < n:
      if a[i] != j:
        count += 1
        i += k - 1
        
      i += 1

    print()

    ans = min(ans, count)

  print(ans)