for _ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))
  d = {i: a.count(i) for i in a}

  k = 0
  for i in d:
    k += d[i] // 2

  print(k)
