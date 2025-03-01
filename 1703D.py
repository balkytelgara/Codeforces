for _ in range(int(input())):
  n = int(input())
  s = [input() for _ in range(n)]
  ans = ""
  f = {}

  for i in s:
    f[i] = 1

  for string in s:
    for i in range(1, len(string)):
      if f.get(string[:i]) and f.get(string[i:]):
        ans += "1"
        break
    else:
      ans += "0"

  print(ans)