for _ in range(int(input())):
  a, b, c = map(int, input().split())
  x = pow(10, max(a, b) - 1)
  y = pow(10, min(a, b) - 1)

  x += pow(10, c - 1)
  
  if a <= b:
    print(min(x, y), max(x, y))
  else:
    print(max(x, y), min(x, y))