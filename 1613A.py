for _ in range(int(input())):
  x1, p1 = map(int, input().split())
  x2, p2 = map(int, input().split())

  mn = min(p1, p2)
  p1 -= mn
  p2 -= mn

  if p1 >= 7:
    print(">")
  elif p2 >= 7:
    print("<")
  else:
    x1 *= pow(10, p1)
    x2 *= pow(10, p2)

    print("=" if x1 == x2 else "<" if x1 < x2 else ">")
    