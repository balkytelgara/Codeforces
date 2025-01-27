"""
Arithmetic sequence
a1 = 6
d = 6
S(n) = (a1 + an) / 2 * n
S(n) = (a1 + a1 + (n - 1) * d) / 2 * n
S(n) = (2a1 + dn - d) / 2 * n
S(n) = (12 + 6n - 6) / 2 * n
S(n) = (12n + 6n^2 - 6n) / 2
S(n) = (6n^2 + 6n) / 2

Final answer: (6n^2 + 6n) / 2 + 1 (that zero hexagon)
"""

n = int(input())
print((6 * n ** 2 + 6 * n) // 2 + 1)