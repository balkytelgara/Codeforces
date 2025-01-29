n, x, y = map(int, input().split())
s = input()

ans = 0
for i in range(n - x, n):
  ans += s[i] != str(int(i == n - y - 1))

print(ans)