n, m = map(int, input().split())

if n == 0 and m != 0:
  print("Impossible")
else:
  if m == 0:
    print(n, n)
  else:
    print(max(n, m), n + m - 1)