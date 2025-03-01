for _ in range(int(input())):
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
  a.sort(reverse=True)

  score = 0
  for i in range(n):
    if i % 2 == 0:
      score += a[i]
    else:
      needed = min(k, a[i - 1] - a[i])
      a[i] += needed
      k -= needed
      score -= a[i]

  print(score)