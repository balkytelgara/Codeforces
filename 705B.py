n = int(input())
a = list(map(int, input().split()))
cumulative = 0

for i in range(1, n + 1):
    curr = a[0]
    cumulative += curr
    rem = cumulative - i
    print(1 if rem & 1 else 2)
    a.pop(0)