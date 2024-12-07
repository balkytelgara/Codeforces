for _ in range(int(input())):
  s = input()

  for i in range(1, len(s)):
    if s[i - 1] == s[i]:
      print(s[i - 1] + s[i])
      break
  else:
    for i in range(1, len(s) - 1):
      if s[i - 1] != s[i] and s[i] != s[i + 1] and s[i - 1] != s[i + 1]:
        print(s[i - 1] + s[i] + s[i + 1])
        break 
    else:
      for i in range(1, len(s) - 2):
        c = s[i - 1] + s[i] + s[i + 1] + s[i + 2]
        if (c.count(c[0]) == 3 and c[1] != c[0]) or \
           (c.count(c[0]) == 3 and c[2] != c[0]) or \
           (c.count(c[0]) == 3 and c[0] != c[3]):
          print(c)
          break
      else:
        print(-1)