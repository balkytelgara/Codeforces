a = [input() for _ in range(8)]
k = a.count("B" * 8)

for i in range(8):
  s = ""
  
  for j in range(8):
    s += a[j][i]

  k += s == "B" * 8

if k == 16:
  k = 8

print(k)