n = int(input())
b = list(range(1, n + 1))
o = b[::2]
e = b[1::2]

if n == 3:
	print(len(o))
	print(*o)
elif n == 2:
	print(1, 1, sep="\n")
elif n == 1:
	print(1, 1, sep="\n")
else:
	print(n)
	print(*(o[::-1] + e[::-1]))