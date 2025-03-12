def solve():
  n = int(input())
  a = list(map(int, input().split()))

  freq = [0] * (n + 1)
  for x in a:
    freq[x] += 1

  len_list = [0] * (n + 1)
  len_list[0] = 1 if freq[a[0]] == 1 else 0
  for i in range(1, n):
    if freq[a[i]] == 1:
      len_list[i] = len_list[i - 1] + 1

  mx = max(len_list)
  if mx == 0:
    print("0")
    return

  for i in range(n):
    if len_list[i] == mx:
      print(i - len_list[i] + 2, i + 1)
      return

for _ in range(int(input())):
  solve()