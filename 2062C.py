for _ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))
  s = sum(a)

  for _ in range(n - 1):
    a.reverse()

    for i in range(len(a) - 1):
      a[i] = a[i + 1] - a[i]

    a.pop()

    s = max(abs(sum(a)), s)

  print(s)