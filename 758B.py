s = input()
d = {s.find(c) % 4: c for c in "RBYG"}
kr = kb = ky = kg = 0

for i in range(len(s)):
  if s[i] == "!":
    match d[i % 4]:
      case "R":
        kr += 1
      case "B":
        kb += 1
      case "Y":
        ky += 1
      case "G":
        kg += 1

print(kr, kb, ky, kg)