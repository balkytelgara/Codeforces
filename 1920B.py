def solve():
  n, k, x = map(int, input().split())
  a = list(map(int, input().split()))

  A = [0] * (n + 1)
  for i in range(1, n + 1):
    A[i] = a[i - 1]
  
  A[1:n + 1] = sorted(A[1:n + 1], reverse=True)

  for i in range(1, n + 1):
    A[i] += A[i - 1]
  
  ans = float('-inf')
  for i in range(k + 1):
    ans = max(ans, A[n] - 2 * A[min(i + x, n)] + A[i])
  
  print(ans)

for _ in range(int(input())): solve()