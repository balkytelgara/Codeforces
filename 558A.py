def solve():
  n = int(input())
  ans = 0
  neg, pos, freq = [], [], {}

  for _ in range(n):
    x, a = map(int, input().split())
    freq[x] = a

    if x > 0:
      pos.append(x)
    else:
      neg.append(x)

  pos.sort(), neg.sort(reverse=True)
  possize, negsize = len(pos), len(neg)

  if possize == negsize:
    for i in range(possize):
      ans += freq[pos[i]] + freq[neg[i]]
  elif possize > negsize:
    for i in range(negsize):
      ans += freq[pos[i]] + freq[neg[i]]
    ans += freq[pos[negsize]]
  else:
    for i in range(possize):
      ans += freq[pos[i]] + freq[neg[i]]
    ans += freq[neg[possize]]

  print(ans)

solve()