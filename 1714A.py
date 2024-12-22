from io import BytesIO
from os import read
from os import fstat

inputstream = BytesIO(
  read(0, fstat(0).st_size)
)

input = inputstream.readline

for _ in range(int(input())):
  n, H, M = map(int, input().split())

  time = 60 * H + M
  md = 24 * 60
  for _ in range(n):
    h, m = map(int, input().split())

    t = 60 * h + m - time
    if (t < 0):
      t += 24 * 60
    md = min(md, t)

  print(md // 60, md % 60)