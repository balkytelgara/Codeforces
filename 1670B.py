for _ in range(int(input())):
  n = int(input())
  s = input()
  kl = input().split()
  k = int(kl[0])
  l = {i: True for i in kl[1:]}

  c, mx = 0, 0

  for i in range(n):
    if l.get(s[i]):
      mx = max(c, mx)
      c = 0
    c += 1

  print(mx)