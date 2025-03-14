for _ in range(int(input())):
  n = int(input())
  a = sorted(map(int, input().split()), reverse=True)

  a1 = 0
  for i in range(0, 2 * n, 2):
    a1 += a[i] - a[i + 1]

  print(a1, *a)