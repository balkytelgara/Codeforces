for _ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))
  f = {}
  e = []
  ans = 0

  for i in range(n):
    if a[i] % 2 == 0 and not f.get(a[i]):
      f[a[i]] = 1
      e.append(a[i])

  e.sort(reverse=True)

  for number in e:
    if f[number]:
      while number % 2 == 0 and number > 0:
        number //= 2
        ans += 1
        if f.get(number):
          f[number] = 0

  print(ans)