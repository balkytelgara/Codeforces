for _ in range(int(input())):
  n, m = map(int, input().split())
  freq = {}
  for i in map(int, input().split()):
    freq[i] = freq.get(i, 0) + 1

  b = sorted(map(int, input().split()), reverse=True)
  for i in b:
    freq[i] = freq.get(i, 0) + 1

  