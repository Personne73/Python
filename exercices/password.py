def check_password(password):
    """
    Teste la robustesse d'un password

    :arg
        password: chaine de caractères
    :return
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
    for i in range(0, len(password)):
        if any(i.isdigit() for i in password):
            if len(password) >= 10 and any(i.islower() for i in password) and any(i.isupper() for i in password):
                return True

    return False


def main():
    result = check_password('QwErTy911poqqqq')
    print(result)


if __name__ == '__main__':
    main()
