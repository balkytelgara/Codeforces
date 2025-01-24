for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    
    for i in range(n - 1, 0, -1):
        if a[i] == a[i - 1]:
            edge = a[i]
            lim = 2 * edge
            a.pop(i)
            a.pop(i - 1)
            break
    else: 
        print(-1)
        continue

    for i in range(1, n - 2):
        if a[i] - a[i - 1] < lim:
            print(edge, edge, a[i - 1], a[i])
            break
    else:
        print(-1)