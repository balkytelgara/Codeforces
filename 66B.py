n = int(input())
a = list(map(int, input().split()))
ans = 0

for i in range(n):
  count = 1
  k = i
  for j in range(i - 1, -1, -1):
    if a[j] <= a[k]:
      count += 1
    else:
      break

    k -= 1

  k = i
  for j in range(i + 1, n):
    if a[j] <= a[k]:
      count += 1
    else:
      break

    k += 1

  ans = max(ans, count)

print(ans)