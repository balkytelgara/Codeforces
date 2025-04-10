n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))
s = [0]
d = {1: 1}

for i in range(n):
  for j in range(s[-1] + 1, s[-1] + a[i] + 1):
    s.append(j)
    d[j] = i + 1

for i in range(m):
  print(d[q[i]])