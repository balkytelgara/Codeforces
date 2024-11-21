s1 = input().split("|")
s2 = list(input())
sz = len(s2)

s = sorted([len(s1[0]), len(s1[1])])
d = max(s) - min(s)

if sz >= d and (sz - d) % 2 == 0:
  s1[len(s1[0]) > len(s1[1])] += "".join(s2[:d])
  s2[:d] = []

  s1[0] += "".join(s2[:len(s2) // 2])
  s1[1] += "".join(s2[len(s2) // 2:])

  print(s1[0], s1[1], sep="|")
else:
  print("Impossible")