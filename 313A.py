n = int(input())

if n >= 0:
  print(n)
else:
  n = str(n)

  if n.startswith("-") and len(n) == 2:
    print(0)
  else:
    if int(n[-2]) <= int(n[-1]):
      print(int(n[:-1]))
    else:
      print(int(n[:-2] + n[-1]))