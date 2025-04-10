for i in range(int(input())):
  n, x = map(int, input().split())
  a = list(map(int, input().split()))
  added = set()
  flag = True
  ans = sum(a)

  for i in a: 
    if i % x == 0:
      added.add((i // x, x))
    else:
      flag = False
      break

  if flag:
    i = 0 
    while True:
      if added[i][0] % x == 0:
        added.add((added[i][0] // x, added[i][1] * x))
        i += 1
      else:
        break

  for i in range(len(added)):
    ans += added[i][0] * added[i][1]

  print(ans)