for _ in range(int(input())):
  n: int = int(input())

  if n % 2 == 0:
    print(n // 2, n // 2)
  else:
    x: str = ""
    y: str = ""
    p: bool = True

    for i in str(n):
      i: int = int(i)
      a: str = str(i // 2)
      b: str = str(i // 2 + i % 2)

      if i % 2 == 0:
        x += a
        y += b
      else:
        if p:
          x += b
          y += a
        else:
          x += a
          y += b

        p = not p

    print(int(x), int(y))