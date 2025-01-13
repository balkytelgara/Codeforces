def solve():
  n = int(input())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))

  k = 0
  need = 0
  margin = 1_000_000_000
  for i in range(n):
    if a[i] < b[i]:
      if k > 0:
        print("NO")
        return
      else:
        k += 1
        need = b[i] - a[i]

  for j in range(n):
    if a[j] >= b[j]:
      margin = min(margin, a[j] - b[j])

  if margin >= need:
    print("YES")
  else:
    print("NO")

for _ in range(int(input())):
  solve()