import os


def scand(r):
    """
    Sépare les fichiers et les répertoires du répertoire passé en argument
    Args:
        r: répertoire à analyser
    Returns:
        Liste des noms de fichier sous forme de chaine de caractères
        Liste des noms de répertoire sous forme de chaine de caractères
    >>> file, directory = scand("C:/Users/treso/Documents/EsieeParis/E2/Cours")
    >>> isinstance(file, list) # vrai si f est une liste
    True
    >>> len(file) == 0
    False
    >>> isinstance(file, list) # vrai si d est une liste
    True
    >>> len(directory) == 0
    False
    """
    # le contenu des répertoires étant dépendant de la configuration
    # les doctests sont limités

    # pour chaque documents listé dans le chemin spécifié de os.listdir(r)
    # si le document du chemin en question qu'on récupère à l'aide de os.path.join(r, doc)
    # est un fichier ( os.path.isfile() ), alors on ajoute le document à la liste
    # même principe pour les répertoires (directory)
    file = [doc for doc in os.listdir(r) if os.path.isfile(os.path.join(r, doc))]
    directory = [doc for doc in os.listdir(r) if os.path.isdir(os.path.join(r, doc))]

    return file, directory


def main():
    file, directory = scand("C:/Users/treso/Documents/EsieeParis/E2/Cours")
    print(file)
    print(directory)


if __name__ == '__main__':
    main()
