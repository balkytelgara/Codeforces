for _ in range(int(input())):
  a, s, b = list(input())

  r = a + s + b
  if (s == "=" and a == b) or \
     (s == ">" and a > b) or \
     (s == "<" and a < b):
    print(r)
    continue

  a, b = int(a), int(b)

  if a == b:
    print(str(a) + "=" + str(b))
  elif a > b:
    print(str(a) + ">" + str(b))
  else:
    print(str(a) + "<" + str(b))
