s = input()

for i in range(97, 123):
  c = chr(i)

  for j in range(len(s) + 1):
    p = s[:j] + c + s[j:]

    if p == p[::-1]:
      print(p)
      break
  else:
    continue

  break
else:
  print("NA")