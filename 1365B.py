for _ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))

  for i in range(n - 1):
    if a[i] <= a[i + 1]:
      continue
    else:
      break
  else:
    print("YES")
    continue

  if b.count(1) > 0 and b.count(0) > 0:
    print("YES")
  else:
    print("NO")