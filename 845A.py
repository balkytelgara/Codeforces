n = int(input())
a = sorted(map(int, input().split()))
f = a[:n]
s = a[n:]

if f[n - 1] == s[0]:
  print("NO")
else:
  print("YES")