for _ in range(int(input())):
  n: int = int(input())
  a: list = list(map(int, input().split()))

  cnt0: int = a.count(0)
  cnt1: int = n - cnt0

  if cnt0 >= n // 2:
    print(cnt0)
    print(*[0] * cnt0)
  else:
    print(cnt1 - cnt1 % 2)
    print(*[1] * (cnt1 - cnt1 % 2))