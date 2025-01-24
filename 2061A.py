for _ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))
  o, e = 0, 0

  for i in a:
    if i % 2 == 0:
      e += 1
    else:
      o += 1

  if e > 0:
    print(o + 1)
  else:
    print(o - 1)