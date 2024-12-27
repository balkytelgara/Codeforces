for _ in range(int(input())):
  n = int(input())
  s = list(input())

  if s[0] == "s":
    s[0] = "."
  if s[-1] == "p":
    s[-1] = "."

  if ("s" not in s) or \
     ("p" not in s):
    print("YES")
  else:
    print("NO")
