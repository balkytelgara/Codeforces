for _ in range(int(input())):
  n, P, l, t = map(int, input().split())

  lb = 0
  rb = n
  totaltasks = n // 7 * 2

  while rb - lb > 1:
    mid = (rb + lb) // 2

    if (mid * lb + min(2 * mid, totaltasks) * t >= P):
      rb = mid
    else:
      lb = mid

  print(n - rb)