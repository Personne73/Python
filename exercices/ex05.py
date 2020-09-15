# Vos import ici


def pal(s):
    """
    Teste si s est un palindrome.

    Args:
        s: chaine de caractères

    Returns:
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

    # Ecriture "bas niveau"
    # i = 0
    # j = len(s) - 1
    # while i < j:
    #     while s[i] == ' ': i +=1
    #     while s[j] == ' ': j -=1
    #     if s[i].lower() != s[j].lower():
    #         return False
    #     i += 1
    #     j -= 1
    # return True
    
    # Ecriture Pythonique (3 lignes max)
    # votre code ici...
    
    return True

def check_password(password):
    """
    Teste la robustesse d'un password

    Args:
        password: chaine de caractères

    Returns:
        True or False

    >>> check_password('A1213pokl')
    False
    >>> check_password('bAse730onE')
    True
    >>> check_password('asasasasasasasaas')
    False
    >>> check_password('QWERTYqwerty')
    False
    >>> check_password('123456123456')
    False
    >>> check_password('QwErTy911poqqqq')
    True
    """
    # votre code ici...
    
    return True

def main():
    # votre code de test ici...
    # 1. appel de la fonction sur un cas particulier
    # 2. affichage de la valeur de retour
    # Par exemple :
    # result = check_password('A1213pokl')
    # print(result)
    pass

if __name__ == '__main__':
    main()
