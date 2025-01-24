for _ in range(int(input())):
  l, r = map(int, input().split())

  if l == r and l == 1:
    print(1)
  else:
    print(r - l)