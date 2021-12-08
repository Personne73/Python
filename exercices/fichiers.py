from zipfile import ZipFile

ARCHIVE = 'meteofrance2014.zip'


def extract_temp(date, code):
    """
    retourne la liste des températures pour la date et la station météo passées en arguments

    Args:
        date: une date au format AAAAMMJJ
        code: code de la station météo

    Returns:
        liste des températures en degrés Celsius

    >>> print(extract_temp('20140109', '07005')) # Abbeville le 9 janvier 2014
    [11.2, 11.6, 11.8, 11.0, 9.6, 8.2, 7.9, 6.8]
    >>> print(extract_temp('20140317', '07110')) # Brest le 17 mars
    [7.2, 7.3, 7.2, 7.5, 8.7, 9.8, 8.5, 7.9]
    >>> print(extract_temp('20140623', '07434')) # Limoges le 23 juin 2014
    [20.2, 17.0, 16.1, 16.1, 18.2, 17.6, 16.3, 15.0]
    >>> print(extract_temp('20140815', '07761')) # Ajaccio le 15 aout 2014
    [18.2, 16.7, 17.8, 25.8, 25.5, 24.9, 22.5, 19.4]
    >>> print(extract_temp('20140703', '89642')) # Terre Adélie le 3 juillet 2014
    [-17.7, -19.2, -18.7, -19.6, -20.4, -20.8, -23.3, -23.3]
    >>> print(extract_temp('20140703', '12345')) # Station inconnue
    []
    >>> print(extract_temp('20150703', '89642')) # date non comprise dans l'archive
    []
    """

    temp = []

    # construction du nom du fichier csv à ouvrir à partir du paramètre 'date'
    filename = "synop." + date[:-2] + ".csv"

    # on ouvre l'archive
    # version pour pc portable :
    myzip = ZipFile('C:/Users/treso/Documents/EsieeParis/E2/Cours/Python/data/meteofrance2014.zip')

    # version pour Zéphyr
    # myzip = ZipFile('D:/Documents/EsieeParis/E2/Cours/Python/data/meteofrance2014.zip')

    # on retourne une liste vide si le fichier n'est pas dans l'archive
    if filename not in myzip.namelist():
        return []

    # je lis le contenu du fichier avec la notation internationnale
    data = myzip.read(filename).decode('utf8')

    data = data.split("\n")  # on split pour creer une liste des lignes du fichier

    # on a besoin des collones 0, 1 et 7 pour le code station, la date et la température
    for line in data[1:]: # pas besoin de parcourir la premier ligne
        line = line.split(";")  # on split les ';' pour transformer chaque ligne en liste
        if code == line[0] and date == line[1][:8]:  # pour avoir les 8 premier caractere de la date
            temp.append(round(float(line[7]) - 273.15, 2))  # on converti la température de Kelvin a °C
            # round pour arrondir les chiffres a virgule

    return temp


def main():
    print(extract_temp('20140109', '07005'))


if __name__ == '__main__':
    main()
