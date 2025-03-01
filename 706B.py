from bisect import bisect_right

n = int(input())
x = sorted(map(int, input().split()))
q = int(input())

for query in range(q):
  print(bisect_right(x, int(input())))