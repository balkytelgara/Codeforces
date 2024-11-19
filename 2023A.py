for _ in range(int(input())):
  n = int(input())
  a = [list(map(int, input().split())) for _ in range(n)]
  a.sort(key=lambda x: sum(x))

  for i in a:
    print(*i, end=' ')
  print()
