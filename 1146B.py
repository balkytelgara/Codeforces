t = input()
r = ""

for i in t:
  if i != "a":
    r += i

s = len(r)
if r[:s // 2] == r[s // 2:] and t[len(t) - s // 2:] == r[:s // 2]:
  print(t[:len(t) - s // 2])
else:
  print(":(")