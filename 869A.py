n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
f = {i: 1 for i in x + y}

pairs = 0
for i in range(n):
  for j in range(n):
    if f.get(x[i] ^ y[j]):
      pairs += 1

if pairs % 2 == 0:
  print("Karen")
else:
  print("Koyomi")