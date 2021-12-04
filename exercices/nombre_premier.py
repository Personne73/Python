# programme pour savoir si un nombre est premier

from math import sqrt

p = int(input("Rentrez un nombre !"))

for d in range(2, int(sqrt(p))+1):
    if p % d == 0:
        print(f"{p} = {d} x {p//d} : False")
        break
else:
    print(p, " : True")
