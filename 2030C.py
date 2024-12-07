for _ in range(int(input())):
  n = int(input())
  s = input()
  w = False

  if s[0] == "1" and s[0] == s[-1]:
    w = True
  for i in range(1, n):
    if s[i - 1] == "1" and s[i - 1] == s[i]:
      w = True
      break
  
  if w:
    print("YES")
  else:
    print("NO")