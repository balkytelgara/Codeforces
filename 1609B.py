n, q = map(int, input().split(' '))
s = list(input())

num = 0
for i in range(n - 2):
  if (''.join(s[i:i + 3]) == 'abc'):
    num += 1

for i in range(q):
  pos, ch = input().split(' ')
  pos = int(pos) - 1

  for j in range(max(0, pos - 2), pos + 1):
    if (''.join(s[j:j + 3]) == 'abc'):
      num -= 1

  s[pos] = ch

  for j in range(max(0, pos - 2), pos + 1):
    if (''.join(s[j:j + 3]) == 'abc'):
      num += 1

  print(num)