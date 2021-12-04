def is_happy(n):
    """
    Vérifie si le nombre passé en paramètre est un nombre heureux

    Args:
        n : nombre entier
    :return:
        True ou False

    >>> is_happy(1)
    True
    >>> is_happy(7)
    True
    >>> is_happy(31)
    True
    >>> is_happy(4)
    False
    """
    n_string = str(n)
    somme = 0
    for c in n_string:
        somme += int(c) ** 2

    if somme == 1:
        return True

    if somme == 4:
        return False

    if somme <= 9:
        return False

    return is_happy(somme)


def main():
    for i in range(0, 100):
        if is_happy(i):
            print(i)


if __name__ == '__main__':
    main()
