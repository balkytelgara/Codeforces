for _ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))
  b = []
  even, odd = [], []

  for i in range(2 * n):
    if a[i] % 2 == 0:
      even.append(i + 1)
    else:
      odd.append(i + 1)

  size_even = len(even)
  size_odd = len(odd)

  for i in range(0, size_even, 2):
    if i + 1 < size_even:
      b.append((even[i], even[i + 1]))

  for i in range(0, size_odd, 2):
    if i + 1 < size_odd:
      b.append((odd[i], odd[i + 1]))

  for i in range(n - 1):
    print(*b[i])