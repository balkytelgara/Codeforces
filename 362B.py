def solve():
  n, m = map(int, input().split())

  if m == 0:
    print("YES")
    return

  a = sorted(map(int, input().split()))
  if a[-1] == n or a[0] == 1:
    print("NO")
  else:
    for i in range(m - 2):
      if (a[i] + 1 == a[i + 1]) and (a[i + 1] + 1 == a[i + 2]):
        print("NO")
        break
    else:
      print("YES")

solve()