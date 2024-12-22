n, m, c = input().split()
n, m = int(n), int(m)

s = [input() for _ in range(n)]
k = 0

for i in range(n):
  for j in range(m):
    if s[i][j] == c:
      l = s[i].find(c)
      r = s[i].rfind(c)

      try:
        if i < n - 1 and i > 0:
          k += len(set(s[i + 1][l:r + 1].replace(".", "")))
          k += len(set(s[i - 1][l:r + 1].replace(".", "")))
        elif i == 0:
          k += len(set(s[i + 1][l:r + 1].replace(".", "")))
        else:
          k += len(set(s[i - 1][l:r + 1].replace(".", "")))

        if r < m - 1 and l > 0:
          k += s[i][l - 1] != "."
          k += s[i][r + 1] != "."
        elif l == 0:
          k += s[i][r + 1] != "."
        else:
          k += s[i][l - 1] != "."
      except:
        pass
      break
  else:
    continue
  break

print(k)