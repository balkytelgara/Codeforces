m = [input() for _ in range(4)]

for i in range(3):
  for j in range(3):
    s = m[i][j] + m[i][j + 1] + m[i + 1][j] + m[i + 1][j + 1]

    if s.count(".") <= 1 or s.count("#") <= 1:
      print("YES")
      exit()
else:
  print("NO")