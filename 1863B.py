for _ in range(int(input())):
  n = int(input())
  a = [0] + list(map(int, input().split()))
  pos = [0] * (n + 1)
  res = 0

  for i in range(1, n + 1):
    pos[a[i]] = i

  for i in range(2, n + 1):
    if pos[i - 1] > pos[i]:
      res += 1

  print(res)