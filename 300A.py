n = int(input())
a = list(map(int, input().split()))
s1 = []
s2 = []
s3 = []

for i in a:
  if i > 0:
    s2.append(i)
  elif i < 0:
    s1.append(i)
  else:
    s3.append(i)

size_s1 = len(s1)
size_s2 = len(s2)
size_s3 = len(s3)

if s2:
  if size_s1 % 2 == 0:
    s3.append(s1[0])
    s1.pop(0)
else:
  s2.append(s1[0])
  s2.append(s1[1])
  s1.pop(0)
  s1.pop(0)

  if (size_s1 - 2) % 2 == 0:
    s3.append(s1[0])
    s1.pop(0)

print(len(s1), *s1)
print(len(s2), *s2)
print(len(s3), *s3)