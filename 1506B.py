def solve():
    n, k = map(int, input().split())
    s = input()
    res = 1
    i = s.find('*')
    
    while True:
        j = min(n - 1, i + k)
        while i < j and s[j] == '.':
            j -= 1
        if i == j:
            break
        res += 1
        i = j

    print(res)

tests = int(input())
for _ in range(tests):
    solve()
