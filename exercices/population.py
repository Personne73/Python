# Vos import ici
import csv
import doctest

# le path du fichier de données
FILENAME = "../data/population.csv"

def read_file(filename):
    """retourne les données sous la forme d'une liste de dictionnaires

    Args:
        filename (str): le nom du fichier de données (n lignes)

    Returns:
        list: n-1 dictionnaires dont les clés sont les champs de la première ligne du fichier
    
    >>> data = read_file(FILENAME)
    >>> type(data)
    <class 'list'>
    >>> len(data)
    140827
    >>> type(data[0])
    <class 'dict'>
    >>> len(data[0])
    15
    >>> data[1000]["Nom Officiel Région"]
    'Grand Est'
    >>> data[5000]["Code Officiel Département"]
    '02'
    >>> data[10000]["Code Officiel Arrondissement Départemental"]
    '001'
    >>> data[25000]["Nom Officiel Commune / Arrondissement Municipal"]
    'Baneuil'
    >>> data[50000]["Population totale"]
    '1898.0'
    >>> data[75000]["Année de recensement"]
    '2018'
    >>> data[100000]["Nom Officiel EPCI"]
    'CC de la Région de Bar-sur-Aube'
    >>> data[125000]["Nom Officiel Département"]
    'Charente-Maritime'
    >>> data[1500]["Nom Officiel Région"]
    'Occitanie'
    >>> data[5500]["Code Officiel Département"]
    '25'
    >>> data[10500]["Code Officiel Arrondissement Départemental"]
    '001'
    >>> data[25500]["Nom Officiel Commune / Arrondissement Municipal"]
    'Fontenoy'
    >>> data[50500]["Population totale"]
    '52.0'
    >>> data[75500]["Année de recensement"]
    '2015'
    >>> data[100500]["Nom Officiel EPCI"]
    'CC de Yenne'
    >>> data[125500]["Nom Officiel Département"]
    'Aube'
    """
    l = []
    # votre code ici
        
    return l


def build_list_departements(data):
    """retourne la liste ordonnée des départements contenus dans les données

    Args:
        data (list): la liste de dictionnaires retournée par read_file()

    Returns:
        list: la liste ordonnée des départements
    
    >>> data = read_file(FILENAME)
    >>> ld = build_list_departements(data)
    >>> type(ld)
    <class 'list'>
    >>> len(ld)
    99
    >>> '15' in ld
    False
    >>> 15 in ld
    False
    >>> 'Cantal' in ld
    True
    >>> 'Corse' in ld
    False
    >>> '20' in ld
    False
    >>> ld[::20]
    ['Ain', 'Creuse', 'Haute-Saône', 'Manche', 'Sarthe']
    >>> ld[5::20]
    ['Ardennes', 'Doubs', 'Hérault', 'Morbihan', 'Seine-et-Marne']
    >>> ld[10::20]
    ['Aveyron', 'Finistère', 'Jura', 'Orne', "Val-d'Oise"]
    >>> ld[15::20]
    ['Charente', 'Haute-Corse', 'Loiret', 'Pyrénées-Orientales', 'Vienne']
    >>> ld[20::20]
    ['Creuse', 'Haute-Saône', 'Manche', 'Sarthe']
    >>> ld[5]
    'Ardennes'
    >>> ld[15]
    'Charente'
    >>> ld[25]
    'Doubs'
    >>> ld[35]
    'Haute-Corse'
    >>> ld[45]
    'Hérault'
    >>> ld[55]
    'Loiret'
    >>> ld[65]
    'Morbihan'
    """
    # votre code ici
    l = []
    return l 
    
def build_list_communes(data):
    """retourne la liste des tuples (code, commune)

    Args:
        data (list): la liste de dictionnaires retournée par read_file()

    Returns:
        list: la liste ordonnées des tuples (code, commune)
    
    >>> data = read_file(FILENAME)
    >>> lc = build_list_communes(data)
    >>> type(lc)
    <class 'list'>
    >>> len(lc)
    35836
    >>> type(lc[999])
    <class 'tuple'>
    >>> len(lc[999])
    2
    >>> lc[999]
    ('02598', 'Pernant')
    >>> type(lc[999][0])
    <class 'str'>
    >>> type(lc[999][1])
    <class 'str'>
    >>> lc[100:103]
    [('01105', 'Civrieux'), ('01106', 'Cize'), ('01107', 'Cleyzieu')]
    >>> lc[900:903]
    [('02499', 'Montbavin'), ('02500', 'Montbrehain'), ('02501', 'Montchâlons')]
    >>> lc[2000:2003]
    [('06089', 'Opio'), ('06090', 'Pégomas'), ('06091', 'Peille')]
    >>> lc[5000:5003]
    [('14712', 'Troarn'), ('14713', 'Montillières-sur-Orne'), ('14713', 'Trois-Monts')]
    >>> lc[10000:10003]
    [('27522', 'Saint-Christophe-sur-Condé'), ('27523', "Saint-Clair-d'Arcey"), ('27524', 'Sainte-Colombe-la-Commanderie')]
    >>> lc[15000:15003]
    [('39138', 'Chemin'), ('39139', 'Chêne-Bernard'), ('39140', 'Chêne-Sec')]
    >>> lc[20000:20003]
    [('54062', 'Benney'), ('54063', 'Bernécourt'), ('54064', 'Bertrambois')]
    >>> lc[25000:25003]
    [('63001', 'Aigueperse'), ('63002', 'Aix-la-Fayette'), ('63003', 'Ambert')]
    >>> lc[30000:30003]
    [('76002', 'Alvimare'), ('76004', 'Ambrumesnil'), ('76005', 'Amfreville-la-Mi-Voie')]
    >>> lc[-3:]
    [('97502', 'Saint-Pierre'), ('97701', 'Saint-Barthélemy'), ('97801', 'Saint-Martin')]
    """
    # votre code ici
    l = []
    return l

def get_pop_commune(data, commune, annee):
    """retourne la population totale d'une commune

    Args:
        data (list): la liste de dictionnaires retournée par read_file()
        commune (str) : la commune considérée
        annee (int): l'année considérée

    Returns:
        int: la population totale

    >>> data = read_file(FILENAME)
    >>> get_pop_commune(data, 'Chaumergy', 2015)
    492
    >>> get_pop_commune(data, 'Chaumergy', 2016)
    498
    >>> get_pop_commune(data, 'Chaumergy', 2017)
    498
    >>> get_pop_commune(data, 'Chaumergy', 2018)
    492
    >>> get_pop_commune(data, 'Chaumergy', 2019)
    
    >>> get_pop_commune(data, 'Aigueperse', 2015)
    2740
    >>> get_pop_commune(data, 'Aigueperse', 2016)
    252
    >>> get_pop_commune(data, 'Aigueperse', 2017)
    2763
    >>> get_pop_commune(data, 'Aigueperse', 2018)
    2790
    >>> get_pop_commune(data, 'Amfreville-la-Mi-Voie', 2015)
    3212
    >>> get_pop_commune(data, 'Amfreville-la-Mi-Voie', 2016)
    3249
    >>> get_pop_commune(data, 'Amfreville-la-Mi-Voie', 2017)
    3302
    >>> get_pop_commune(data, 'Amfreville-la-Mi-Voie', 2018)
    3354
    >>> get_pop_commune(data, 'Trifouilly-les-Oies', 2015)
    
    >>> get_pop_commune(data, 'Trifouilly-les-Oies', 2016)
    
    >>> get_pop_commune(data, 'Trifouilly-les-Oies', 2017)
    
    >>> get_pop_commune(data, 'Trifouilly-les-Oies', 2018)
    
    """
    pop = None
    
    return pop

def build_dict_departements(lc, sd):
    """
    lc : la liste des communes retournée par build_list_communes()
    sd : l'ensemble des départements retourné par build_set_departements()

    Retourne un dictionnaire dont la clé est le département, et la valeur une liste [nombre de communes, population totale]
    
    >>> data = read_file("communes.csv")
    >>> sd = build_set_departements(data)
    >>> lc = build_list_communes(data)
    >>> dd = build_dict_departements(lc, sd)
    >>> type(dd)
    <class 'dict'>
    >>> len(dd)
    100
    >>> dd['18']
    [290, 319693]
    >>> dd['21']
    [706, 543648]
    >>> dd['27']
    [675, 612518]
    >>> dd['53']
    [261, 318095]
    """
    # votre code ici
    
    return dict()
    
def stat_by_dpt(dd, dpt):
    """
    dd : le dictionnaire retourné par build_dict_departements()
    dpt : le département concerné (str)

    Retourne une liste [nombre de communes, population totale]
    >>> data = read_file("communes.csv")
    >>> sd = build_set_departements(data)
    >>> lc = build_list_communes(data)
    >>> dd = build_dict_departements(lc, sd)
    >>> sbd = stat_by_dpt(dd, '87')
    >>> type(sbd)
    <class 'list'>
    >>> len(sbd)
    2
    >>> sbd[1]
    384411
    >>> sbd[0]
    201
    >>> sbd = stat_by_dpt(dd, '77')
    >>> sbd[1]
    1387830
    >>> sbd[0]
    513
    >>> sbd = stat_by_dpt(dd, 'Corse')
    >>> sbd is None
    True
    """
    # votre code ici
    l = []
    
    return l

def main():
    # votre code de test ici
    # le code ci dessous est exécuté avec la commande :
    #   python communes.py
    pass
    # data = read_file(FILENAME)
    # print(data[:10])
    # l = build_list_departements(data)
    # print(l)
    # c = build_list_communes(data)
    # print(c[::2000])
    # p = get_pop_commune(data, 'Chaumergy', 2018)
    # print(p)
    
# Ne pas modifier le code ci-dessous
if __name__ == '__main__':
    dt = False
    # dt = not dt
    if dt:
        doctest.run_docstring_examples(get_pop_commune, globals())
    else:
        main()
