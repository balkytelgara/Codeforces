for _ in range(int(input())):
  n, k = map(int, input().split())
  p = [0] * n

  i = n // k
  while i > 0:
    p[i * k - 1] = i
    i -= 1

  l = list(range(n, n // k, -1))
  for i in range(n):
    if (i + 1) % k != 0:
      p[i] = l.pop(0)

  for i in p:
    print(i, end=' ')
  print()