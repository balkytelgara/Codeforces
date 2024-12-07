s = [input() for _ in range(4)]
c = "xx.", "x.x", ".xx"
for i in s:
  for j in c:
    if j in i:
      print("YES")
      break
  else:
    continue
  break
else:
  r = ["".join(s[j][i] for j in range(4)) for i in range(4)]
  for i in r:
    for j in c:
      if j in i:
        print("YES")
        break
    else:
      continue
    break
  else:
    if (s[0][0] + s[1][1] + s[2][2] in c) or \
       (s[1][1] + s[2][2] + s[3][3] in c) or \
       (s[1][0] + s[2][1] + s[3][2] in c) or \
       (s[0][1] + s[1][2] + s[2][3] in c) or \
       (s[3][0] + s[2][1] + s[1][2] in c) or \
       (s[2][1] + s[1][2] + s[0][3] in c) or \
       (s[2][0] + s[1][1] + s[0][2] in c) or \
       (s[3][1] + s[2][2] + s[1][3] in c):
      print("YES")
    else:
      print("NO")