x, y = map(int, input().split())
print([x, y, y - x, -x, -y, x - y][(int(input()) - 1) % 6] % (10 ** 9 + 7))