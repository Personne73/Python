FILENAME = "presidentielle2017.csv"

import csv


def read_file(filename):
    """
    Retourne le contenu de filename

    Args:
        str filename : le nom du fichier

    Returns:
        list : le contenu du fichier sous la forme d'une liste de chaines de caractères

    >>> data = read_file(FILENAME)
    >>> isinstance(data, list)
    True
    >>> len(data)
    35720
    >>> len(data[666])
    377
    >>> data[666][121:136]
    'MACRON;Emmanuel'
    >>> data[667][79:92]
    'LE PEN;Marine'
    >>> data[668][121:139]
    'MÉLENCHON;Jean-Luc'
    >>> data[669][79:94]
    'FILLON;François'
    >>> data[670][214:235]
    'DUPONT-AIGNAN;Nicolas'
    >>> data[671][256:268]
    'HAMON;Benoît'
    >>> data[672][302:317]
    'POUTOU;Philippe'
    >>> data[673][346:362]
    'ARTHAUD;Nathalie'
    >>> data[674][359:376]
    'CHEMINADE;Jacques'
    >>> data[675][409:422]
    'LASSALLE;Jean'
    >>> data[676][291:310]
    'ASSELINEAU;François'
    >>> data[677][12:18]
    'Epagny'
    >>> data[678][63:65]
    '71'
    >>> data[679][23:59]
    '418;55;13,16;363;86,84;3;0,72;0,83;0'
    >>> data[35291][:29]
    'ZA;Guadeloupe;110;La Désirade'
    >>> data[35322][:32]
    'ZB;Martinique;209;Fort-de-France'
    >>> data[35349][:21]
    'ZC;Guyane;302;Cayenne'
    >>> data[35385][:30]
    'ZD;La Réunion;416;Saint-Pierre'
    >>> data[35401][:23]
    'ZM;Mayotte;508;Dzaoudzi'
    >>> data[35428][:32]
    'ZN;Nouvelle-Calédonie;818;Nouméa'
    >>> data[35447][:35]
    'ZP;Polynésie française;14;Bora-Bora'
    >>> data[35493][:44]
    'ZS;Saint-Pierre-et-Miquelon;502;Saint-Pierre'
    >>> data[35494][:38]
    'ZW;Wallis et Futuna;1;Wallis-Et-Futuna'
    >>> data[35496][:49]
    'ZX;Saint-Martin/Saint-Barthélemy;801;Saint-Martin'
    >>> data[35520][:45]
    'ZZ;Français établis hors de France;25;Bangkok'
    """
    l = []
    # votre code ici
    with open(filename, 'r', encoding='utf8') as file:
        reader = file.readlines()

        for line in reader:
            l.append(line)

    return l


def parse_header(data):
    """
    Retourne les indices de colonnes correspondant aux noms des candidats

    Args:
        list data : la liste des lignes du fichier de données

    Returns:
        list : les indices de colonnes correspondant aux noms des candidats

    >>> data = read_file(FILENAME)
    >>> indices = parse_header(data)
    >>> isinstance(indices, list)
    True
    >>> len(indices)
    11
    >>> indices[0]
    20
    >>> indices[1]
    27
    >>> indices[2]
    34
    >>> indices[3]
    41
    >>> indices[4]
    48
    >>> indices[5]
    55
    >>> indices[6]
    62
    >>> indices[7]
    69
    >>> indices[8]
    76
    >>> indices[9]
    83
    >>> indices[10]
    90
    """
    indices = []
    # votre code ici

    list_colum = data[1].split(";")

    i = 20
    indices.append(20)

    while 1:
        i += 7
        if i <= len(list_colum):
            indices.append(i)
        else:
            break

    return indices


def build_candidates_list(data, indices):
    """
    Retourne la liste des noms des candidats par ordre alphabétique

    Args:
        list data : la liste des lignes du fichier de données
        list indices : les indices de colonnes correspondant aux noms des candidats

    Returns:
        list : la liste des noms des candidats par ordre alphabétique

    >>> data = read_file(FILENAME)
    >>> indices = parse_header(data)
    >>> candidats = build_candidates_list(data, indices)
    >>> isinstance(candidats, list)
    True
    >>> len(candidats)
    11
    >>> len(candidats[4])
    6
    >>> len(candidats[7])
    6
    >>> len(candidats[8])
    6
    >>> len(candidats[10])
    6
    >>> all([ candidat[0].isupper() for candidat in candidats ])
    True
    >>> candidats[0]
    'Arthaud'
    >>> candidats[1]
    'Asselineau'
    >>> candidats[2]
    'Cheminade'
    >>> candidats[3]
    'Dupont-Aignan'
    >>> candidats[4]
    'Fillon'
    >>> candidats[5]
    'Hamon'
    >>> candidats[6]
    'Lassalle'
    >>> candidats[7]
    'Le Pen'
    >>> candidats[8]
    'Macron'
    >>> candidats[9]
    'Mélenchon'
    >>> candidats[10]
    'Poutou'
    """
    candidats = []
    # votre code ici
    list_colum = data[1].split(";")
    list_name = []

    for indice in indices:
        list_name.append(list_colum[indice])

    list_name.sort()

    for elt in list_name:
        word = elt.title()
        candidats.append(word)

    return candidats


def build_insee_code(dpt_code, city_code):
    """
    Retourne le code INSEE sur 5 caractères

    Args:
        str dpt_code : le code du département
        str city_code : le code de la ville

    Returns:
        str : le code INSEE sur 5 caractères

    >>> build_insee_code(87,85)
    
    >>> build_insee_code('87',85)
    
    >>> build_insee_code(87,'85')
    
    >>> build_insee_code('87','85')
    '87085'
    >>> build_insee_code(4,70)
    
    >>> build_insee_code('4',70)
    
    >>> build_insee_code(4,'70')
    
    >>> build_insee_code('4','70')
    '04070'
    >>> build_insee_code(13,5)
    
    >>> build_insee_code('13',5)
    
    >>> build_insee_code(13,'5')
    
    >>> build_insee_code('13','5')
    '13005'
    >>> build_insee_code('2B',231)
        
    >>> build_insee_code('2B','231')
    '2B231'
    """
    res = ""
    # votre code ici
    if not isinstance(dpt_code, str) or not isinstance(city_code, str):
        return

    if isinstance(dpt_code, str):
        dpt_code = str(dpt_code)
        if len(dpt_code) == 1:
            res = '0' + dpt_code
        else:
            res = dpt_code

    res2 = ""
    if isinstance(city_code, str):
        city_code = str(city_code)

        if len(city_code) == 1:
            res2 = '00' + city_code
        elif len(city_code) == 2:
            res2 = '0' + city_code
        elif len(city_code) == 3:
            res2 = city_code

    res += res2
    return res


def get_cities(data):
    """
    Retourne la liste des tuples (commune, code INSEE) présents dans les données

    Args:
         list data : la liste des lignes du fichier de données

    Returns:
        list : la liste des tuples (commune, code INSEE)

    >>> data = read_file(FILENAME)
    >>> cities = get_cities(data)
    >>> isinstance(cities, list)
    True
    >>> len(cities)
    35719
    >>> cities[666]
    ('Dommiers', '02267')
    >>> "é" in cities[::3500][0][0]
    True
    >>> int(cities[::3500][1][1])%2
    0
    >>> "-" in cities[::3500][2][0]
    True
    >>> int(cities[::3500][3][1])//9
    3123
    >>> "z" in cities[::3500][4][0]
    True
    >>> cities[::3500][5][1].endswith('222')
    True
    >>> "h" in cities[::3500][6][0] and cities[::3500][6][1].startswith('56')
    True
    >>> sum([int(digit) for digit in cities[::3500][7][1]])
    23
    >>> len(cities[::3500][8][0])
    10
    >>> cities[::3500][9][0][1] * int(cities[::3500][9][1][4])
    'iiii'
    >>> "".join(reversed(cities[::3500][10][0])).lower()
    'nosiamlam-lieur'
    """
    cities = []
    # votre code ici
    for line in data[1:]:
        line = line.split(";")
        cities.append( (line[3], build_insee_code(line[0], line[2]) ) )

    return cities


def build_city_dict(row, candidats):
    """
    Construit un dictionnaire à partir d'une ligne de résultat

    Args:
        str row : une ligne du fichier de données
        list candidats : la liste des noms des candidats

    Returns:
        dict : les données formattées dans un dictionnaire

    >>> data = read_file(FILENAME)
    >>> indices = parse_header(data)
    >>> candidats = build_candidates_list(data, indices)

    >>> row = "1;Ain;2;L'Abergement-de-Varey;209;25;11,96;184;88,04;6;2,87;3,26;2;0,96;1,09;176;84,21;95,65;2;F;LE PEN;Marine;48;22,97;27,27;3;M;MACRON;Emmanuel;37;17,7;21,02;11;M;FILLON;François;34;16,27;19,32;9;M;MÉLENCHON;Jean-Luc;33;15,79;18,75;4;M;HAMON;Benoît;13;6,22;7,39;1;M;DUPONT-AIGNAN;Nicolas;6;2,87;3,41;5;F;ARTHAUD;Nathalie;2;0,96;1,14;6;M;POUTOU;Philippe;2;0,96;1,14;10;M;ASSELINEAU;François;1;0,48;0,57;7;M;CHEMINADE;Jacques;0;0;0;8;M;LASSALLE;Jean;0;0;0"
    >>> d = build_city_dict(row, candidats)
    >>> len(d)
    19
    >>> 
    >>> d['Ville']
    "L'Abergement-de-Varey"
    >>> d['Code']
    '01002'
    >>> d['Inscrits']
    209
    >>> d['Abstensions']
    25
    >>> d['Votants']
    184
    >>> d['Blancs']
    6
    >>> d['Nuls']
    2
    >>> d['Exprimés']
    176
    >>> d['Le Pen']
    48
    >>> d['Macron']
    37
    >>> d['Fillon']
    34
    >>> d['Mélenchon']
    33
    >>> d['Hamon']
    13
    >>> d['Dupont-Aignan']
    6
    >>> d['Arthaud']
    2
    >>> d['Poutou']
    2
    >>> d['Asselineau']
    1
    >>> d['Cheminade']
    0
    >>> d['Lassalle']
    0
    """
    d = dict()
    # votre code ici
    row = row.split(";")
    d["Ville"] = row[3]
    d["Code"] = build_insee_code(row[0], row[2])
    d["Inscrits"] = int(row[4])
    d["Abstensions"] = int(row[5])
    d["Votants"] = int(row[7])
    d["Blancs"] = int(row[9])
    d["Nuls"] = int(row[12])
    d["Exprimés"] = int(row[15])

    return d


def build_country_dict(data, candidats):
    """
    Retourne le dictionnaire des résultats globaux

    Args:
        list data : la liste des lignes du fichier de données
        list candidats : la liste des noms des candidats par ordre alphabétique

    Returns:
    dict : le dictionnaire des résultats

    >>> data = read_file(FILENAME)
    >>> indices = parse_header(data)
    >>> candidats = build_candidates_list(data, indices)
    >>> results = build_country_dict(data, candidats)
    >>> keys = list(results.keys())
    >>> len(keys)
    35719
    >>> i = keys.index('77083')
    >>> i
    30416
    >>> results[keys[i]]["Ville"]
    'Champs-sur-Marne'
    >>> results[keys[i]]["Inscrits"]
    14486
    >>> results[keys[i]]["Abstensions"]
    2993
    >>> results[keys[i]]["Votants"]
    11493
    >>> results[keys[i]]["Blancs"]
    219
    >>> results[keys[i]]["Macron"]
    3111
    >>> results[keys[i]]["Le Pen"]
    1573
    """
    res = dict()
    # votre code ici

    return res


def extract_results(results, cities):
    """
    Retourne les résultats cumulés pour les villes passées en argument

    Args:
        dict results : le dictionnaire global des résultats, tel que retourné par la fonction build_country_dict()
        list cities : une liste des codes INSEE définissant le périmètre de l'extraction

    Returns:
        dict : le dictionnaire des résultats cumulés

    >>> data = read_file(FILENAME)
    >>> indices = parse_header(data)
    >>> candidats = build_candidates_list(data, indices)
    >>> results = build_country_dict(data, candidats)
    >>> cities = get_cities(data)
    >>> subset_of_cities = [ '77083']
    >>> res = extract_results(results, subset_of_cities)
    >>> res['Exprimés']
    11202
    >>> res['Arthaud']
    53
    >>> res['Asselineau']
    145
    >>> res['Cheminade']
    30
    >>> res['Dupont-Aignan']
    464
    >>> res['Fillon']
    1624
    >>> res['Hamon']
    898
    >>> res['Lassalle']
    91
    >>> res['Le Pen']
    1573
    >>> res['Macron']
    3111
    >>> res['Mélenchon']
    3109
    >>> res['Poutou']
    104
    >>> subset_of_cities = [ t[1] for t in cities if t[1].startswith('77')]
    >>> res = extract_results(results, subset_of_cities)
    >>> res['Exprimés']
    680591
    >>> res['Arthaud']
    3706
    >>> res['Asselineau']
    8195
    >>> res['Cheminade']
    1247
    >>> res['Dupont-Aignan']
    41505
    >>> res['Fillon']
    120968
    >>> res['Hamon']
    38772
    >>> res['Lassalle']
    5182
    >>> res['Le Pen']
    155521
    >>> res['Macron']
    157314
    >>> res['Mélenchon']
    141827
    >>> res['Poutou']
    6354
    """
    res = dict()
    # votre code ici

    return res


class Votes():
    """
    Classe regroupant les résultats électoraux d'une commune

    Attributs:
        int : 'Abstensions'
        int : 'Blancs'
        int : 'Exprimés'
        int : 'Inscrits'
        int : 'Nuls'
        dict : 'Résultats'
        str : 'Ville'
        int : 'Votants'

    >>> data = read_file(FILENAME)
    >>> indices = parse_header(data)
    >>> candidats = build_candidates_list(data, indices)
    >>> results = build_country_dict(data, candidats)
    >>> d = results['87085']
    >>> v = Votes(d)
    >>> v.Abstensions
    18371
    >>> v.Blancs
    1155
    >>> v.Exprimés
    58282
    >>> v.Inscrits
    78450
    >>> v.Nuls
    642
    >>> v.Ville
    'Limoges'
    >>> v.Votants
    60079
    >>> v.Resultats['Macron']
    16958
    >>> v.Resultats['Mélenchon']
    13370
    >>> v.Resultats['Fillon']
    9484
    >>> v.Resultats['Le Pen']
    8460
    >>> v.Resultats['Hamon']
    5318
    >>> v.participation()
    76.58
    >>> names = v.get_top3_names()
    >>> names
    ['Macron', 'Mélenchon', 'Fillon']
    >>> for name in names:
    ...     print(name, v.get_abs_res_by_name(name))
    Macron 16958
    Mélenchon 13370
    Fillon 9484
    >>> for name in names:
    ...     print(name, v.get_rel_res_by_name(name))
    Macron 28.23
    Mélenchon 22.25
    Fillon 15.79
    """
    pass
    # votre code ici


def main():
    pass
    # votre code ici
    data = read_file(FILENAME)
    # print(data[674][359:376])
    indices = parse_header(data)
    # print(indices)
    candidats = build_candidates_list(data, indices)
    build_insee_code(4, 70)
    cities = get_cities(data)
    row = "1;Ain;2;L'Abergement-de-Varey;209;25;11,96;184;88,04;6;2,87;3,26;2;0,96;1,09;176;84,21;95,65;2;F;LE PEN;Marine;48;22,97;27,27;3;M;MACRON;Emmanuel;37;17,7;21,02;11;M;FILLON;François;34;16,27;19,32;9;M;MÉLENCHON;Jean-Luc;33;15,79;18,75;4;M;HAMON;Benoît;13;6,22;7,39;1;M;DUPONT-AIGNAN;Nicolas;6;2,87;3,41;5;F;ARTHAUD;Nathalie;2;0,96;1,14;6;M;POUTOU;Philippe;2;0,96;1,14;10;M;ASSELINEAU;François;1;0,48;0,57;7;M;CHEMINADE;Jacques;0;0;0;8;M;LASSALLE;Jean;0;0;0"
    d = build_city_dict(row, candidats)
    print(d)


if __name__ == "__main__":
    main()
