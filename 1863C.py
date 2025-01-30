for _ in range(int(input())):
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
  mex = (n * (n + 1) // 2) - sum(a)

  for i in range(n):
    temp = a[i]
    a[i] = mex
    mex = temp

  a.append(mex)

  last = (k - 1) % (n + 1)
  for i in range(n + 1 - last, n + 1):
    print(a[i], end=" ")

  for i in range(n - last):
    print(a[i], end=" ")
    
  print()