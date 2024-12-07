with open("input.txt", "r") as f:
  lines = f.read().split("\n")
  f.close()

n, m = map(int, lines[0].split())
r = ""

for i in range(n + m):
  if n > 0 and m > 0:
    if i % 2 == 0:
      r += "B"
      n -= 1
    else:
      r += "G"
      m -= 1
  else:
    if n > 0:
      r += "B" * n
      n = 0
    else:
      r += "G" * m
      m = 0

with open("output.txt", "w") as f:
  f.write(r)
  f.close()