from math import ceil

n = int(input())
print(("abcd" * int(ceil(n / 4)))[:n])