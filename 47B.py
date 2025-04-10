s1 = input()
s2 = input()
s3 = input()

a = s1.count("A>") + s1.count("<A") + \
    s2.count("A>") + s2.count("<A") + \
    s3.count("A>") + s3.count("<A")

b = s1.count("B>") + s1.count("<B") + \
    s2.count("B>") + s2.count("<B") + \
    s3.count("B>") + s3.count("<B")

c = s1.count("C>") + s1.count("<C") + \
    s2.count("C>") + s2.count("<C") + \
    s3.count("C>") + s3.count("<C")

if a > b and a > c:
  print("CBA" if b > c else "BCA" if c > b else "Impossible")
elif b > a and b > c:
  print("CAB" if a > c else "ACB" if c > a else "Impossible")
else:
  print("BAC" if a > b else "ABC" if b > a else "Impossible")