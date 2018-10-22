import os

def scand(r):
    """
    Sépare les fichiers et les répertoires du répertoire passé en argument

    Args:
        r: répertoire à analyser

    Returns:
        Liste des noms de fichier sous forme de chaine de caractères
        Liste des noms de répertoire sous forme de chaine de caractères
    >>> f, d = scand('C:\Windows')
    >>> isinstance(f, list) # vrai si f est une liste
    True
    >>> len(f) == 0
    False
    >>> isinstance(f, list) # vrai si d est une liste
    True
    >>> len(d) == 0
    False
    """
    # le contenu des répertoires étant dépendant de la configuration
    # les doctests sont limités

    f = []
    d = []
    return f, d
    
def searchext(l):
    """
    Identifie les extensions de la liste de fichiers passée en argument

    Args:
        l : liste des noms de fichier sous forme de chaine de caractères

    Returns:
        Liste des extensions sous forme de chaine de caractères
        
    >>> l = searchext(['ARJ.PIF', 'atiogl.xml', 'ativpsrm.bin', 'bfsvc.exe'])
    >>> isinstance(l, list) # vrai si l est une liste
    True
    >>> print(l)
    ['pif', 'xml', 'bin', 'exe']
    >>> l = searchext(['HelpPane.exe', 'hh.exe', 'HPMProp.INI', 'IE9_main.log'])
    >>> isinstance(l, list) # vrai si l est une liste
    True
    >>> print(l)
    ['exe', 'exe', 'ini', 'log']
    >>> l = searchext(['win.ini', 'WindowsShell', 'WindowsUpdate.log', 'winhelp.exe'])
    >>> isinstance(l, list) # vrai si l est une liste
    True
    >>> print(l)
    ['ini', 'log', 'exe']
    """
    
    e = []
    return e

def guess_language(text):
    """
    Estimation du langage utilisé dans la chaine de caractères passée en 
    argument par analyse de fréquence

    Args:
        text: chaine de caractères

    Returns:
        'english', 'french', 'german' or 'spanish'
        
    >>> guess_language("aaaaaaaabcccddddeeeeeeeeeeeeeffgghhhhhhiiiiiiikllllmmnnnnnnnoooooooopprrrrrrsssssstttttttttuuuvwwyy")
    'english'
    >>> guess_language("aaaaaaaaaaaabbccccdddddeeeeeeeeeeeeefgghiiiiiiilllllmmmnnnnnnnoooooooooopppqrrrrrrrsssssssstttttuuuvy")
    'spanish'
    >>> guess_language("aaaaaaabbcccdddddeeeeeeeeeeeeeeeeffggghhhhhiiiiiiiklllmmmnnnnnnnnnnoooprrrrrrrssssssssttttttuuuuuvwwz")
    'german'
    >>> guess_language("aaaaaaaabcccddddeeeeeeeeeeeeeeeeefghiiiiiiiijlllllmmmnnnnnnnoooooopppqrrrrrrrsssssssstttttttuuuuuuvv")
    'french'
    """
    
    return None   

def main():
    # votre code de test ici...
    # 1. appel de la fonction sur un cas particulier
    # 2. affichage de la valeur de retour
    pass

if __name__ == '__main__':
    main()