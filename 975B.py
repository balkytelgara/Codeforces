a = list(map(int, input().split()))
mx = 0

for i in range(14):
  b = a.copy()
  temp = b[i]

  b[i] = 0

  for j in range(14):
    b[j] += temp // 14
  
  temp %= 14
  k = i + 1

  while temp:
    temp -= 1

    if k == 14:
      k = 0
    
    b[k] += 1
    k += 1
  
  mx = max(mx, sum([i for i in b if i % 2 == 0]))

print(mx)