import csv
import json
from collections import namedtuple


def build_stations_dict(csvfile):
    """
    retourne un dictionnaire des stations météo du fichier passé en argument

    Args:
        csvfile: un fichier au format csv contenant une liste de stations météo

    Returns:
        dictionnaire de namedtuple des informations relatives aux stations météo

    >>> d = build_stations_dict('D:/Documents/EsieeParis/E2/Cours/Python/data/stations-meteo.csv')
    >>> print(d['NICE'])
    Station(ID='07690', Latitude=43.648833, Longitude=7.209, Altitude=2)
    >>> print(d['BELLE ILE-LE TALUT'])
    Station(ID='07207', Latitude=47.294333, Longitude=-3.218333, Altitude=34)
    >>> print(d['CAYENNE-MATOURY'])
    Station(ID='81405', Latitude=4.822333, Longitude=-52.365333, Altitude=4)
    >>> print(d['NICE'].Latitude)
    43.648833
    """
    # Création d'un dictionnaire vide pour stocker nos infos
    d = dict()

    # création du namedtuple qui sera utilisé comme valeur du dictionnaire
    Station = namedtuple('Station', ['ID', 'Latitude', 'Longitude', 'Altitude'])

    # ouverture de mon fichier csv
    with open(csvfile, 'r') as file:
        # lecture du contenu de mon fichier donc de mon csv
        reader = csv.reader(file, delimiter=';')

        # pour chaque ligne de mon csv
        for line in reader:
            if line[2] == "Latitude":
                continue
            # print(line)
            # j'ajoute dans mon dictionnaire la clé (nom de la station) et la valeur (namedtuple)
            d[line[1]] = Station(line[0], float(line[2]), float(line[3]), int(line[4]))

    return d


if __name__ == '__main__':
    d = build_stations_dict('D:/Documents/EsieeParis/E2/Cours/Python/data/stations-meteo.csv')
    print(d['NICE'])
    print(d['BELLE ILE-LE TALUT'])
    print(d['CAYENNE-MATOURY'])
    print(d['NICE'].ID)
    print(d['NICE'].Latitude)
    print(d['NICE'].Longitude)
    print(d['NICE'].Altitude)
