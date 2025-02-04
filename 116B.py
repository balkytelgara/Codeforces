n, m = map(int, input().split())
cmap = ["." + input() + ".." for _ in range(n)]
cmap.append(".." * m)
cmap.append(".." * m)
ans = 0

for i in range(n):
  for j in range(1, m + 1):
    if cmap[i][j] == "W":
      if cmap[i - 1][j] == "P" or \
         cmap[i + 1][j] == "P" or \
         cmap[i][j - 1] == "P" or \
         cmap[i][j + 1] == "P":
        ans += 1

print(ans)