s = input()

if len(s) % 2 != 0:
  print(-1)
else:
  x, y = 0, 0

  for i in s:
    if i == "U":
      y += 1
    elif i == "D":
      y -= 1
    elif i == "L":
      x += 1
    else:
      x -= 1

  print((abs(x) + abs(y)) // 2)