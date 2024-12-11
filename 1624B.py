for _ in range(int(input())):
  a, b, c = map(int, input().split())

  na = b - (c - b)
  if na >= a and na % a == 0 and na != 0:
    print("YES")
    continue

  nb = a + (c - a) // 2
  if nb >= nb and (c - a) % 2 == 0 and nb % b == 0 and nb != 0:
    print("YES")
    continue

  nc = a + 2 * (b - a)
  if nc >= c and nc % c == 0 and nc != 0:
    print("YES")
    continue

  print("NO")