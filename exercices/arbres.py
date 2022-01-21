import csv

FILENAME = "arbresremarquablesparis.csv"


def read_file(filename):
    """Read file content

    Args:
        filename (str) : nom du fichier

    Returns:
        list : liste des dictionnaires (un par ligne de données)

    >>> data = read_file(FILENAME)
    >>> isinstance(data, list)
    True
    >>> len(data)
    178
    >>> d = data[0] 
    >>> isinstance(d, dict)
    True
    >>> l = list(d.keys())
    >>> 'LIBELLEFRANCAIS' in l
    True
    >>> 'ARRONDISSEMENT' in l
    True
    >>> 'CIRCONFERENCE EN CM' in l
    True
    >>> 'HAUTEUR EN M' in l
    True
    >>> 'Geo point' in l
    True
    >>> d = data[18]
    >>> d['LIBELLEFRANCAIS']
    'Figuier'
    >>> d['ARRONDISSEMENT']
    'PARIS 13E ARRDT'
    >>> d['CIRCONFERENCE EN CM']
    '120.0'
    >>> d['HAUTEUR EN M']
    '4.0'
    >>> d['Geo point']
    '48.82884091038866,2.349764627345979'
    """
    # Votre code ici
    
    return None


def get_data_keys(data):
    """Extract dict keys

    Args:
        data (list) : data returned by read_file()

    Returns:
        list : keys of dict built by read_file()

    >>> data = read_file(FILENAME)
    >>> keys = get_data_keys(data)
    >>> isinstance(keys, list)
    True
    >>> len(keys)
    19
    >>> keys[1]
    'LIBELLEFRANCAIS'
    >>> keys[7]
    'ARRONDISSEMENT'
    >>> keys[11]
    'CIRCONFERENCE EN CM'
    >>> keys[12]
    'HAUTEUR EN M'
    >>> keys[18]
    'Geo point'
    """
    # Votre code ici

    return None


def get_trees_filtered_by_size(data, criteria, operator, value):
    """Filter trees by size (circumference or height)

    Args:
        data (list) : data returned by read_file()
        criteria (str) : circumference or height corresponding key
        operator (str) : relational operator
        value (float) : value used for comparison and filtering

    Returns:
        list : trees corresponding to numerical criteria

    >>> data = read_file(FILENAME)
    >>> f = get_trees_filtered_by_size(data, 'ARRONDISSEMENT', '>', 'PARIS 2E ARRDT')
    
    >>> f = get_trees_filtered_by_size(data, 'LIBELLEFRANCAIS', '>', 'Chêne')
    
    >>> f = get_trees_filtered_by_size(data, 'Geo point', '>', 48.51236547854)

    >>> f = get_trees_filtered_by_size(data, 'CIRCONFERENCE EN CM', '>', 600)
    >>> len(f)
    6
    >>> f[0]['LIBELLEFRANCAIS']
    'Platane'
    >>> f[0]['ARRONDISSEMENT']
    'PARIS 19E ARRDT'
    >>> f[0]['CIRCONFERENCE EN CM']
    '686.0'
    >>> f[0]['HAUTEUR EN M']
    '30.0'
    >>> f[0]['Geo point']
    '48.880335483410086,2.381305309812792'
    >>> f[1]['LIBELLEFRANCAIS']
    'Platane'
    >>> f[1]['ARRONDISSEMENT']
    'PARIS 7E ARRDT'
    >>> f[1]['CIRCONFERENCE EN CM']
    '695.0'
    >>> f[1]['HAUTEUR EN M']
    '25.0'
    >>> f[1]['Geo point']
    '48.85783876010566,2.293318739569995'
    >>> f = get_trees_filtered_by_size(data, 'HAUTEUR EN M', '<', 15)
    >>> len(f)
    55
    >>> f[10]['LIBELLEFRANCAIS']
    'Catalpa'
    >>> f[10]['ARRONDISSEMENT']
    'BOIS DE VINCENNES'
    >>> f[10]['CIRCONFERENCE EN CM']
    '289.0'
    >>> f[10]['HAUTEUR EN M']
    '10.0'
    >>> f[10]['Geo point']
    '48.82007112336596,2.435166264692187'
    >>> f[21]['LIBELLEFRANCAIS']
    'Hêtre'
    >>> f[21]['ARRONDISSEMENT']
    'PARIS 5E ARRDT'
    >>> f[21]['CIRCONFERENCE EN CM']
    '90.0'
    >>> f[21]['HAUTEUR EN M']
    '3.0'
    >>> f[21]['Geo point']
    '48.844887526406524,2.353669163189394'
    >>> f = get_trees_filtered_by_size(data, 'HAUTEUR EN M', '<=', 15)
    >>> f[21]['LIBELLEFRANCAIS']
    'Chicot du Canada'
    >>> f[21]['ARRONDISSEMENT']
    'PARIS 20E ARRDT'
    >>> f[21]['CIRCONFERENCE EN CM']
    '155.0'
    >>> f[21]['HAUTEUR EN M']
    '11.0'
    >>> f[21]['Geo point']
    '48.86151633861924,2.399065981839158'
    >>> f = get_trees_filtered_by_size(data, 'CIRCONFERENCE EN CM', '>=', 400)
    >>> f[21]['LIBELLEFRANCAIS']
    'Hêtre'
    >>> f[21]['ARRONDISSEMENT']
    'PARIS 14E ARRDT'
    >>> f[21]['CIRCONFERENCE EN CM']
    '400.0'
    >>> f[21]['HAUTEUR EN M']
    '20.0'
    >>> f[21]['Geo point']
    '48.822604055366384,2.336701218855207'
    >>> f = get_trees_filtered_by_size(data, 'CIRCONFERENCE EN CM', '=', 200)
    >>> f[0]['LIBELLEFRANCAIS']
    'Catalpa'
    >>> f[0]['ARRONDISSEMENT']
    'PARIS 16E ARRDT'
    >>> f[0]['CIRCONFERENCE EN CM']
    '200.0'
    >>> f[0]['HAUTEUR EN M']
    '3.0'
    >>> f[0]['Geo point']
    '48.84758185002834,2.25327790355166'
    """
    # Votre code ici
    return None


def get_trees_filtered_by_string(data, criteria, value):
    """Filter trees by string

    Args:
        data (list) : data returned by read_file()
        criteria (str) : all criteria except numerical ones
        value (str) : value used for comparison and filtering

    Returns:
        list : trees corresponding to string criteria

    >>> data = read_file(FILENAME)
    >>> f = get_trees_filtered_by_string(data, 'ARRONDISSEMENT', 'PARIS 21E ARRDT')
    >>> len(f)
    0
    >>> f = get_trees_filtered_by_string(data, 'ARRONDISSEMENT', 'BOIS DE VINCENNES')
    >>> len(f)
    24
    >>> f[10]['LIBELLEFRANCAIS']
    'Chêne'
    >>> f[10]['ARRONDISSEMENT']
    'BOIS DE VINCENNES'
    >>> f[10]['CIRCONFERENCE EN CM']
    '245.0'
    >>> f[10]['HAUTEUR EN M']
    '20.0'
    >>> f[10]['Geo point']
    '48.818389186647245,2.437918513675584'
    >>> f = get_trees_filtered_by_string(data, 'LIBELLEFRANCAIS', 'Cèdre')
    >>> len(f)
    8
    >>> f[0]['LIBELLEFRANCAIS']
    'Cèdre'
    >>> f[0]['ARRONDISSEMENT']
    'PARIS 14E ARRDT'
    >>> f[0]['CIRCONFERENCE EN CM']
    '155.0'
    >>> f[0]['HAUTEUR EN M']
    '20.0'
    >>> f[0]['Geo point']
    '48.831999798675646,2.325830070246111'
    """
    # Votre code ici
    return None


def get_short_description(tree):
    """Build a short description string

    Args:
        tree (dict): tree characteristics

    Returns:
        string: formatted description string

    >>> tree = {'IDBASE': '2002353.0', \
            'LIBELLEFRANCAIS': 'Araucaria', \
            'GENRE': 'Araucaria', \
            'ESPECE': 'araucana', \
            'ADRESSE': 'PARC DE BAGATELLE - ALLEE DE LONGCHAMP / ROUTE DE SEVRES A NEUILLY', \
            'TYPEEMPLACEMENT': 'Arbre', \
            'DOMANIALITE': 'Jardin', \
            'ARRONDISSEMENT': 'BOIS DE BOULOGNE', \
            'COMPLEMENTADRESSE': '16-23', \
            'NUMERO': '', \
            'IDEMPLACEMENT': '000701003', \
            'CIRCONFERENCE EN CM': '182.0', \
            'HAUTEUR EN M': '11.0', \
            'STADEDEVELOPPEMENT': 'Adulte', \
            'PEPINIERE': 'Inconnue', \
            'VARIETE OU CULTIVAR': '', \
            'DATEPLANTATION': '1907-01-01T01:09:21+01:00', \
            'REMARQUABLE': 'OUI', \
            'Geo point': '48.871681148770165,2.249232652751458'}
    >>> s = get_short_description(tree)
    >>> d, f = 0, 25
    >>> s[d:f]
    'Araucaria                '
    >>> d, f = 25, 45
    >>> s[d:f]
    'BOIS DE BOULOGNE    '
    >>> d, f = 45, 62
    >>> s[d:f]
    'h(m) = 11.0      '
    >>> d, f = 62, 80
    >>> s[d:f]
    'd(cm) = 182.0     '
    >>> d, f = 80, 96
    >>> s[d:f]
    'lat = 48.8717   '
    >>> d, f = 96, 112
    >>> s[d:f]
    'lon = 2.2492    '

    """
    # Votre code ici
    return None


def fmc(data):
    """Multi criteria filtering

    Args:
        data (list): data returned by read_file()

    Returns:
        list : short descriptions of filtered trees

    >>> data = read_file(FILENAME)
    >>> l = fmc(data)
    >>> isinstance(l, list)
    True
    >>> len(l)
    4
    >>> isinstance(l[0], str)
    True
    >>> "Orme                     PARIS 4E ARRDT      h(m) = 10.0      d(cm) = 167.0     lat = 48.8521   lon = 2.3508    " in l
    True
    >>> "Cèdre                    PARIS 2E ARRDT      h(m) = 18.0      d(cm) = 290.0     lat = 48.8789   lon = 2.1864    " in l
    False
    """
    # Votre code ici
    return None


def main():
    # Votre code de test ici
    pass
    # data = read_file(FILENAME)
    # print(data)
    # keys = get_data_keys(data)
    # print(keys)
    # f = get_trees_filtered_by_size(data, 'CIRCONFERENCE EN CM', '>', 600)
    # print(f)
    # f = get_trees_filtered_by_string(data, 'ARRONDISSEMENT', 'PARIS 7E ARRDT')
    # print(f)
    # tree = data[0]
    # s = get_short_description(tree)
    # print(s)
    # r = fmc(data)
    # print(r)


if __name__ == "__main__":
    main()