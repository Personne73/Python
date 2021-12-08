# liste des extentions
import os
from contenu_repertoire import scand


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
    # ancienne version du code
    # ext = []

    # for file in l:
    #    name, extension = os.path.splitext(file)
    #    extension = extension.replace(".", "")
    #    if extension:  # verifie si la chaine n'est pas vide donc si extentions vaut True, cad 1
    #        ext.append(extension.lower())

    # nouvelle version de l'exo
    # fonction splitext(string) pour split le nom d'un fichier de son extension
    # on supprime le '.' puisqu'on ne veut que les extensions et on met en minuscule
    # on parcourt chaque élément de la liste l et on ajoute dans la liste ext l'extension (case à l'indice 1)
    # si la chaine contenant l'extention n'est pas vide (nom sans extensions donc retourne une string vide)

    return [os.path.splitext(file)[1].replace('.', '').lower() for file in l if os.path.splitext(file)[1]]


def main():
    # extensions = searchext(['ARJ.PIF', 'atiogl.xml', 'ativpsrm.bin', 'bfsvc.exe'])
    file, directory = scand("C:/Users/treso/Documents/EsieeParis/E2")
    print(file)
    extensions = searchext(file)
    print(extensions)


if __name__ == '__main__':
    main()
