a, b = map(int, input().split())
r = 1
while a != b and r:
  a += 1
  r = r * a % 10

print(r)