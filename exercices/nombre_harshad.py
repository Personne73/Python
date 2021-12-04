def is_harshad(n: int):
    """
    Vérifie si le nombre passé en paramètre est un nombre de Harshard

    Args:
        n : nombre entier
    :return:
        True ou False

    >>> is_harshad(12)
    True
    >>> is_harshad(20)
    True
    >>> is_harshad(25)
    False
    >>> is_harshad(54)
    True
    >>> is_harshad(79)
    False
    """
    n_string = str(n)  # on converti le nombre en chaine
    somme = 0
    for c in n_string:
        somme += int(c)  # on ajoute à la somme la conversion d'un caractère en entier

    if n % somme == 0:
        return True

    return False


def main():
    for i in range(10, 100):
        if is_harshad(i):
            print(i)


if __name__ == '__main__':
    main()
