s = input()
t = input()
p = ""
c = 0

for i in range(len(s)):
  if s[i] == t[i]:
    p += s[i]
  else:
    c += 1

    if c % 2:
      p += s[i]
    else:
      p += t[i]

print(p if c % 2 == 0 else "impossible")  