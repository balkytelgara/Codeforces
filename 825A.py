n = int(input())
s = input()

k = 0
for i in s:
  if i == "1":
    k += 1
  else:
    print(k, end='')
    k = 0
else:
  print(k)