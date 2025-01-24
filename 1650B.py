for _ in range(int(input())):
  l, r, a = map(int, input().split())
  ans = r // a + r % a
  s = r // a * a - 1
  if s >= l:
    ans = max(ans, s // a + s % a)

  print(ans)