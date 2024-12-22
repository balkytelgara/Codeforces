n, k = map(int, input().split())
s = list(range(1, n + 1))

s = s[n - k:][::-1] + s[:n - k]
print(*s)