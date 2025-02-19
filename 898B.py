n = int(input())
a = int(input())
b = int(input())

t = n // a + 1
for i in range(0, t + 1):
  m = i * a
  if (n - m) % b == 0 and n - m >= 0:
    print("YES")
    print(i, (n - m) // b)
    break
else:
  print("NO")