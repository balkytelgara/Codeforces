def digitsum(n: int) -> int:
    res = 0
    while n:
        res += n % 10
        n //= 10

    return res

k = int(input())
for i in range(1, int(1.25 * 10 ** 7)):
    if digitsum(i) == 10:
        if k > 0:
            k -= 1

        if k == 0:
            print(i)
            break