with open("input.txt", "r") as f:
  lines = f.read().split("\n")
  f.close()

n, m = map(int, lines[0].split())

r = ""

def func(x, a, b):
  s = [a] * (n + m)
  for i in range(1, n + m, 2):
    if x > 0:
      s[i] = b
      x -= 1
    else:
      break

  return "".join(s)

r = func(min(n, m), "G" if n <= m else "B", "B" if n <= m else "G")
print(r, file=open("output.txt", "w"))