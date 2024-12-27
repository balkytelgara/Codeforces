for _ in range(int(input())):
  n, d = map(int, input().split())


  for i in range(1, 10, 2):
    if int(str(d) * i) % i == 0:
      print(i, end=' ')
  print()