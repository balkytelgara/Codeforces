for _ in range(int(input())):
  n = int(input())
  s = input()
  ans = 0
  a = []

  for i in range(n):
    if s[i] == "L":
      ans += i
      a.append((n - 1 - i) - i)
    else:
      ans += n - (i + 1)
      a.append(i - (n - 1 - i))

  a.sort(reverse=True)

  for i in range(n):
    if a[i] > 0:
      ans += a[i]
    print(ans, end=" ")
  print()