from math import log
 
x, y = map(int, input().split())
a, b = y * log(x), x * log(y)

if abs(a - b) < 1e-8:
	print('=')
elif a < b:
	print('<')
else:
	print('>')