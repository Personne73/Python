FILENAME = "../data/mots.txt"

def est_dans(mot, ensemble):
    """
    Retourne une chaine de caractère exprimant la vérité de "mot" est dans "l'ensemble"

    Args:
        mot (str)
        ensemble : une séquence ou un set de chaînes de caractères

    Returns:
        str : la vérité de "mot" est dans "l'ensemble"
    """
    # votre code ici
    return None

def read_file(filename):
    # votre code ici
    return None

if __name__ == "__main__":
    mots = read_file(FILENAME)
    
    # liste

    liste_mots = [ ]
    print("la liste contient", len(liste_mots), "mots")
    
    print(liste_mots[24499])

    # sets

    tout = { }

    for mot in ["chronophage", "procrastinateur", "dangerosité", "gratifiant"]:
        pass
    print()

    mots_7lettres = { }
    print(len(mots_7lettres), "mots de 7 lettres")
    print()

    mots_avec_k = { }
    print(len(mots_avec_k), "mots contenant un k")
    print()

    mots_7lettres_avec_k = {}
    print(len(mots_7lettres_avec_k), "mots de 7 lettres contenant un k")
    print()

    mots_avec_w = { }
    print(len(mots_avec_w), "mots contenant un w")
    print()

    subset = set()
    print(len(subset), "mots contenant un k et un w")
    print()

    mots_avec_z = { }
    print(len(mots_avec_z), "mots contenant un z")
    print()

    mots_commencant_par_z = { }
    print(len(mots_commencant_par_z), "mots commençant par z")    
    print()

    mots_terminant_par_z = { }
    print(len(mots_terminant_par_z), "mots terminant par z")    
    print()

    mots_avec_z_en_position_non_terminale = { }
    print(len(mots_avec_z_en_position_non_terminale), "mots avec z en position non terminale")
    print()

    subset = set()
    print(len(subset), "mots avec z en position non terminale contenant un k")
    print(subset)
    print()
    
    subset = set()
    print(len(subset), "mots avec z en position non terminale contenant un w")
    print(subset)
