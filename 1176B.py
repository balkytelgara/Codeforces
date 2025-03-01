for _ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))
  f = {0: 0, 1: 0, 2: 0}

  for i in a:
    f[i % 3] += 1

  ans = f[0]
  mn = min(f[1], f[2])
  ans += mn
  f[1] -= mn
  f[2] -= mn
  ans += (f[1] + f[2]) // 2

  print(ans)