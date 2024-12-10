for _ in range(int(input())):
  n = int(input())
  h = list(map(int, input().split()))

  need, have = 0, 0

  for i in range(n):
    need += i
    have += h[i]

    if have < need:
      print("NO")
      break
  else:
    print("YES")