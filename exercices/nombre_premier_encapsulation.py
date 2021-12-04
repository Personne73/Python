# encapsulation du code du nombre premier du chapitre 1

from math import sqrt


def est_premier(p):
    """
    Retourne si le nombre passé en paramètre est premier ou non

    :arg
        p : le nombre à tester

    :return:
        True si c'est premier
        False si ce n'est pas premier

    >>> est_premier(1)
    1 : True
    True
    >>> est_premier(25)
    25 = 5 x 5 : False
    False
    >>> est_premier(127)
    127 : True
    True
    """
    for d in range(2, int(sqrt(p)) + 1):
        if p % d == 0:
            print(f"{p} = {d} x {p // d} : False")
            return False
    else:
        print(p, ": True")
        return True


# help(est_premier)



