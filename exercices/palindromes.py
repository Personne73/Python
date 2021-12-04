def pal(s):
    """
    Teste si s est un palindrome.

    :arg
        s: chaine de caractères
    :return:
        True or False

    >>> pal("ressasser")
    True
    >>> pal("Hannah")
    True
    >>> pal("Engage le jeu que je le gagne")
    True
    >>> pal("Esope reste ici et se repose")
    True
    >>> pal("Elu par cette crapule")
    True
    >>> pal("Cette phrase n'est pas un palindrome")
    False
    """

    # s[::-1] la chaine à l'envers

    s = s.lower().replace(" ", "")
    return s == s[::-1]


def main():
    result = pal("Engage le jeu que je le gagne")
    print(result)


if __name__ == '__main__':
    main()
