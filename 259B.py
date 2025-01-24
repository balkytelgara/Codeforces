x11, x12, x13 = map(int, input().split())
x21, x22, x23 = map(int, input().split())
x31, x32, x33 = map(int, input().split())

s = (x12 + x13 + x21 + x23 + x31 + x32) // 2

x11 = s - x12 - x13
x22 = s - x21 - x23
x33 = s - x31 - x32

print(x11, x12, x13)
print(x21, x22, x23)
print(x31, x32, x33)