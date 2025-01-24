from itertools import combinations

for _ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))

  for i in range(n - 1):
    for comb in combinations([a[i], a[i - 1]], 3):
      a, b, c = comb

      if a + b > c and \
         a + c > b and \
         b + c > a:
         print("YES")
         break
    else:
      continue
    break
  else:
    print("NO")