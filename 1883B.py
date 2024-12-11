for _ in range(int(input())):
  n, k = map(int, input().split())
  s = input()

  x = 0
  for i in set(s):
    if s.count(i) % 2 == 1:
      x += 1

  if x > k + 1:
    print("NO")
  else:
    print("YES")