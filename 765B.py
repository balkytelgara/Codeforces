s = input()
f = "a"

for i in range(len(s)):
  if s[i] == f:
    f = chr(ord(f) + 1)
  elif s[i] < f:
    continue
  else:
    print("NO")
    break 
else:
  print("YES")