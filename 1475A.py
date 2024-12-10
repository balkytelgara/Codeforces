for _ in range(int(input())):
  n = int(input())
  
  if n % 2 == 1:
    print("YES")
  else:
    while n != 1:
      if n % 2 == 1:
        print("YES")
        break
      
      n //= 2
    else:
      print("NO")