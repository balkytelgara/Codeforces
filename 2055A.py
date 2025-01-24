for _ in range(int(input())):
  n, a, b = map(int, input().split())

  if a % 2 == b % 2:
    print("YES")
  else:
    print("NO")