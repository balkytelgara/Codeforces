def solve():
  for _ in range(int(input())):
    n = int(input())
    l = [0] * n
    r = [0] * n
    mark = [[False] * (n + 1) for _ in range(n + 1)] 
    
    for i in range(n):
      l[i], r[i] = map(int, input().split())
      mark[l[i]][r[i]] = True

    for i in range(n):
      for j in range(l[i], r[i] + 1):
        if (j == l[i] or mark[l[i]][j - 1]) and (j == r[i] or mark[j + 1][r[i]]):
          print(l[i], r[i], j)
          break

solve()