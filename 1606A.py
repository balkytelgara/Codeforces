for _ in range(int(input())):
  s = input()

  if s[0] == s[-1]:
    print(s)
  else:
    print(s[0] + s[1:-1] + s[0])