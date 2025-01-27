for _ in range(int(input())):
  n, T = map(int, input().split())
  c = 0
  for i in input().split():
    i = int(i)

    if T % 2 == 0 and i == T // 2:
      r = c % 2
      c += 1
    elif i * 2 < T:
      r = 0
    else:
      r = 1

    print(r, end=' ')
  print()