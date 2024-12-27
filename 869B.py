a, b = map(int, input().split())

u = 1
for i in range(b - a, b + 1):
  u *= i

print(u // a)
