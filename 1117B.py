n, m, k = map(int, input().split())
a = sorted(map(int, input().split()))
ans = 0

x = a[-1]
y = a[-2]
print((m // (k + 1)) * (x * k + y) + (m % (k + 1)) * x)