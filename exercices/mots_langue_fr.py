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
    if mot in ensemble:
        return True

    return False


def read_file(filename):
    # premier version
    # with open(filename, mode='r', encoding='utf8') as file:
    #    s = file.read().split("\n")

    # return s
    return open(filename, mode='r', encoding='utf8').read()


if __name__ == "__main__":
    mots = read_file(FILENAME)

    # liste

    liste_mots = mots.split("\n")

    print(liste_mots[24499])
    print(liste_mots[28281])
    print(liste_mots[57305])
    print(liste_mots[118091])
    print(liste_mots[199316])
    print(liste_mots[223435])
    print(liste_mots[336455])

    # sets

    tout = {word for word in liste_mots}
    print(tout)

    mots = ["chronophage", "procrastinateur", "dangerosité", "gratifiant"]
    for word in mots:
        print(word, "est dans la liste : ", est_dans(word, tout))

    mots_7lettres = {word for word in liste_mots if len(word) == 7}
    print(f"Il y a {len(mots_7lettres)} ayant 7 lettres")

    mots_avec_k = {word for word in liste_mots if 'k' in word}
    print(f"Il y a {len(mots_avec_k)} mots avec un 'k'")

    mots_7lettres_avec_k = {word for word in liste_mots if word in mots_7lettres and word in mots_avec_k}
    print(f"Il y a {len(mots_7lettres_avec_k)} mots de 7 lettres avec un 'k'")

    mots_avec_w = {word for word in liste_mots if 'w' in word}
    print(f"Il y a {len(mots_avec_w)} mots avec un 'w'")

    mots_avec_k_et_w = {word for word in liste_mots if word in mots_avec_k and word in mots_avec_w}
    print(f"Il y a {len(mots_avec_k_et_w)} mots avec un 'k' et un 'w'")

    mots_avec_z = {word for word in liste_mots if 'z' in word}
    print(f"Il y a {len(mots_avec_z)} mots contenant un 'z'")

    mots_commencant_par_z = {word for word in liste_mots if 'z' == word[0]}
    print(f"Il y a {len(mots_commencant_par_z)} mots commencant par un 'z'")

    mots_terminant_par_z = {word for word in liste_mots if 'z' == word[len(word)-1]}
    print(f"Il y a {len(mots_terminant_par_z)} mots terminant par un 'z'")

    mots_avec_z_en_position_non_terminale = {word for word in liste_mots if word not in mots_commencant_par_z
                                             and word not in mots_terminant_par_z and word in mots_avec_z}
    print(f"Il y a {len(mots_avec_z_en_position_non_terminale)} mots comportant un 'z' en position non terminale")

    mots_avec_z_en_position_non_terminale_et_un_k = {word for word in liste_mots if word in mots_avec_z_en_position_non_terminale
                                                     and word in mots_avec_k}
    print(f"Il y a {len(mots_avec_z_en_position_non_terminale_et_un_k)} avec un 'z' en position non terminale comportant aussi un 'k'")
