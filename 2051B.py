for _ in range(int(input())):
  n, a, b, c = map(int, input().split())
  s = a + b + c
  k = n // s
  d = n - k * s

  if d > 0 and d <= a:
    print(3 * k + 1)
  elif d > a and d <= b + a:
    print(3 * k + 2)
  elif d > a + b and d <= a + b + c:
    print(3 * k + 3)
  else:
    print(3 * k)