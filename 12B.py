n = input()
m = input()

d = sorted(map(int, n))
zeros = d.count(0)
z = ['0'] * zeros

if zeros == len(n):
  if n == m:
    print("OK")
  else:
    print("WRONG_ANSWER")
else:
  r = str(d[zeros]) + ''.join(z) + ''.join(map(str, d[zeros + 1:]))

  if r == m:
    print("OK")
  else:
    print("WRONG_ANSWER")