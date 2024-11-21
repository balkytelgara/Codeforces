n = int(input())
b = list(map(int, input().split()))
mx = max(b)

cnt = [0] * 6000
for i in range(n):
  cnt[b[i]] += 1

s = set(b)

left, right = [], []

for i in s:
  if cnt[i] > 0 and i < mx:
    right.append(i)
    cnt[i] -= 1

for i in s:
  if cnt[i] > 0 and i < mx:
    left.append(i)

left.sort(), right.sort(reverse=True)

print(1 + len(left) + len(right))
print(*left, mx, *right)