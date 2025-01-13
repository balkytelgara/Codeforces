for _ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))

  d = [0] * (n + 1)

  for i in range(n):
    if a[i] < n:
      d[a[i]] += 1
    else:
      d[n] = 1_000_000

  g = True
  for i in range(1, n + 1):
    if d[i] > d[i - 1]:
      g = False
      break

  print("YES" if g else "NO")