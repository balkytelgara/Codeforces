from math import ceil

for _ in range(int(input())):
  hc, dc = map(int, input().split())
  hm, dm = map(int, input().split())
  k, w, a = map(int, input().split())

  for i in range(0, k + 1):
    attack, armor = i, k - i
    t1 = ceil(hm / (dc + attack * w))
    t2 = ceil((hc + armor * a) / dm)

    if t1 <= t2:
      print("YES")
      break
  else:
    print("NO")