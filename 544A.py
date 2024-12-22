k = int(input())
q = input()

ans = []
curr = ""
used = set()

for i in q:
  if i not in used:
    if len(curr) > 0:
      ans.append(curr)

    curr = ""
    curr += i
    used.add(i)
  else:
    curr += i

ans.append(curr)

if len(ans) < k:
  print("NO")
else:
  print("YES")

  for i in range(k, len(ans)):
    ans[k - 1] += ans[i]

  for i in range(k):
    print(ans[i])