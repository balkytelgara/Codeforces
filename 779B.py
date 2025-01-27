n, k = input().split()
k = int(k)
if len(n) < k:
  print(len(n) - 1)
else:
  ans = 0

  for i in n[::-1]:
    if i == '0':
      k -= 1
    else:
      ans += 1
      continue

    if k == 0:
      break

  if k > 0:
    print(len(n) - 1)
  else:
    print(ans)