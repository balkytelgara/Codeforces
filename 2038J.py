n = int(input())
people = 0

for _ in range(n):
  t, v = input().split()
  v = int(v)

  if t == "P":
    people += v
  else:
    if people < v:
      print("YES")
    else:
      print("NO")

    people -= min(people, v)
