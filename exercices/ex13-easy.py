# Vos imports ici..
import urllib.request
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    # Votre classe ici
    def __init__(self):
        super().__init__(self) # on initialise la super classe
        # un attribut de type structure de donnees pour stocker les informations pertinentes
        # un attribut booleen qui sera True lorsque le parser 
        #      pointera sur la donnée recherchée. False sinon

    def handle_starttag(self, tag, attrs):
        # par défaut le booleen est False
        # si c'est le bon type de balise
        #     si les autres conditions sont réunies
        #         alors le booleen passe à True
        

    def handle_endtag(self, tag):
        # si on sort du bon type de balise
        #     le booleen passe à False

    def handle_data(self, data):
        # si le booleen est True
        #     on rajoute la donnée à la structure de donnees
        

def scrap_imdb(html_data):
    """
    Extrait la liste de film contenue dans html_data.

    Args:
        html_data: source de la page html

    Returns:
        Liste de films
    """
    # Votre code ici...
    # on crée une instance de MyHTMLParser
    # on appelle la méthode feed() sur cette instance
    # on retourne l'attribut qui contient les données
    
        
def main(url):
    """
    >>> with open("IMDb.html", mode='r', encoding='utf8') as f: html_data = f.read()
    >>> movies =  scrap_imdb(html_data)
    >>> for m in movies[:5]: print(m)
    Les évadés
    Le parrain
    Le parrain, 2ème partie
    The Dark Knight: Le chevalier noir
    12 hommes en colère
    >>> for m in movies[-5:]: print(m)
    Lagaan
    L'ultime razzia
    Gangs of Wasseypur
    La douceur de vivre
    In the Mood for Love
    """
    # Votre code ici...
    
    # proxy_address = 'http://147.215.1.189:3128/'
    # proxy_handler = urllib.request.ProxyHandler({'http': proxy_address})
    # opener = urllib.request.build_opener(proxy_handler)
    # urllib.request.install_opener(opener)
    
    # Open URL
    
    # on essaye d'ouvrir l'url et de lire/décoder le code html qu'elle contient
    # sinon on renvoie un message d'erreur (il y a peut être un problème de proxy)
    
    # on appelle la fonction scrap_imdb() en lui passant le contenu de l'url en argument
    
    # on balaye la structure de données renvoyée par scrap_imdb() pour affichage
    
    return None

if __name__ == '__main__':
    # on appelle la fonction main() en lui passant l'url concernée en argument
    main('http://www.imdb.com/chart/top?ref_=nv_ch_250_4')