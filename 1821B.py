for _ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))

  diffl, diffr = -1, -1
  for i in range(n):
    if a[i] != b[i]:
      diffr = i

      if diffl == -1:
        diffl = i

  while diffl > 0 and b[diffl - 1] <= b[diffl]:
    diffl -= 1

  while diffr < n - 1 and b[diffr + 1] >= b[diffr]:
    diffr += 1

  print(diffl + 1, diffr + 1)