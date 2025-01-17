for _ in range(int(input())):
  n, q = map(int, input().split())
  a = list(map(int, input().split()))
  p = [a[0]] + [0] * (n - 1)
  
  for i in range(1, n):
    p[i] = p[i - 1] + a[i]

  s = p[-1]

  for _ in range(q):
    l, r, k = map(int, input().split())
    l -= 1
    r -= 1

    ans = s - (p[r] - p[l] + a[l]) + (r - l + 1) * k
    
    if ans % 2 != 0:
      print("YES", ans)
    else:
      print("NO")