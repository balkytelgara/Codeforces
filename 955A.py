from math import ceil
 
hh, mm = map(int, input().split())
H, D, C, N = map(int, input().split())
 
if hh < 20:
  f = ceil(H / N) * C
  H += (1200 - (hh * 60 + mm)) * D
  s = ceil(H / N) * C * .8
  print(min(f, s))
else:
  print(ceil(H / N) * C * .8)