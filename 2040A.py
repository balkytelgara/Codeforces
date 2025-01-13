def solve():
  n, k = map(int, input().split())
  a = list(map(int, input().split()))

  for i in range(n):
    for j in range(n):
      if i != j and abs(a[i] - a[j]) % k != 0:
        print("YES", i + 1, j + 1)
        return

  print("NO")

for _ in range(int(input())):
  solve()