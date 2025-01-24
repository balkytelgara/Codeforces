def solve():
  n = int(input())
  a = list(map(int, input().split()))
  q = int(input())
  b = [a]

  for _ in range(n):
    f = {}
    for i in b[-1]:
      f[i] = f.get(i, 0) + 1

    t = [f[i] for i in b[-1]]
    b.append(t)

  for _ in range(q):
    x, k = map(int, input().split())

    print(b[min(k, len(b) - 1)][x - 1])

for _ in range(int(input())):
  solve()