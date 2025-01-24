def solve():
  s = input()
  names = ['Danil', 'Olya', 'Slava', 'Ann', 'Nikita']
  ans = 0

  for name in names:
    ans += s.count(name)

  if ans == 1:
    print("YES")
  else:
    print("NO")
solve()