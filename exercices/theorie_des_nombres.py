from nombre_premier_encapsulation import est_premier

n = 1

# premier point de l'exo : nombre de Fermat non premier
while est_premier((2 ** (2 ** n)) + 1):
    n += 1
    res = (2 ** (2 ** n)) + 1

print(f"Le premier nombre de Fermat qui n'est pas premier est pour n = {n}, nombre non premier = {res}")

# deuxième point de l'exo  : nombre premier suivant
n = int(input("Entrez un entier"))
a = n

while not est_premier(n + 1):
    n += 1

print(f"Le premier nombre premier après n = {a} est {n + 1}")

# point trois de l'exo : couple de nombres premiers jumeaux
p = int(input("Entrez un autre entier"))
a = p
n = p + 1

while 1:
    if est_premier(p):
        # print("test 1")
        if est_premier(n) and n - p == 2:
            print(f"Le premier couple de nombres premiers jumeaux après l'entier {a} est le couple ({p},{n})")
            break
        elif est_premier(n) and n - p > 2:
            p += 1
            # print("test 3")
        else:
            n += 1
            # print("test 4")
    else:
        p += 1
        # print("test 5")

# point quatre de l'exo : nombre premier de Germain
p = int(input("Entrez un 3e entier"))
a = p

while 1:
    if est_premier(p) and est_premier(2 * p + 1):
        print(f"Le premier nombre premier de Germain après n = {a} est {p}")
        break
    p += 1
