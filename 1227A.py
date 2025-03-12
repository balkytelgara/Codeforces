for _ in range(int(input())):
  lmax, rmin = 0, 1e9
  for _ in range(int(input())):
    l, r = map(int, input().split())
    lmax = max(lmax, l)
    rmin = min(rmin, r)

  print(max(0, lmax - rmin))