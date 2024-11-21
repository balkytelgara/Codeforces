n = int(input())
a = list(map(int, input().split()))

o = 0
for i in a:
  if i % 2 == 1:
    o += 1

if o > 0:
  print("First")
else:
  print("Second")