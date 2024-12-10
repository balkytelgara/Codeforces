n = int(input())
a = map(int, input().split())
o, e = 0, 0

for i in a:
  if i % 2 == 0:
    e += 1
  else:
    o += 1

print(min(o, e))