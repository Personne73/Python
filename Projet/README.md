# Le mini projet Open Data

Selon l'unité d'enseignement que vous suivez, vous pouvez ne pas être concerné par le mini projet. 

## Descriptif

Le mini projet se déroule dans un environnement Open Data. Selon `Wikipedia <https://fr.wikipedia.org/wiki/Open_data>`_, *l'open data ou donnée ouverte est une donnée numérique d'origine publique ou privée. Elle peut être notamment produite par une collectivité, un service public (éventuellement délégué) ou une entreprise. Elle est diffusée de manière structurée selon une méthode et une licence ouverte garantissant son libre accès et sa réutilisation par tous, sans restriction technique, juridique ou financière.*

L'objectif du mini projet est de recueillir, d'analyser et de présenter des données publiques dans un secteur d'intérêt général tel que la météorologie, la santé publique, la démographie, la finance, l'économie, la politique, le sport, la culture, etc... Le choix des données sur lesquelles vous pouvez travailler vous appartient, sous réserve qu'elles satisfassent aux contraintes énoncées ci dessous.

## Accès aux données

Les données doivent être accessibles publiquement via une page web ou un fichier au format quelconque. Le(s) pointeur(s) vers les ressources doi(ven)t être fourni(s). Un bonus valorisera les programmes implémentant un accès dynamique aux données.

## Caractéristiques des données

Dans la très grande majorité des cas, l'ensemble des données (dataset) est présenté sous la forme d'un certain nombre O d'observations (les lignes du fichier ou de la page HTML) contenant chacune un certain nombre D de données numériques ou catégorielles (les colonnes du fichier ou de la page HTML). Ce dataset doit impérativement posséder les propriétés suivantes:

- Le dataset doit posséder un nombre suffisamment grand d'observations O pour que le tracé d'un histogramme ait du sens (typiquement plusieurs centaines). Ainsi les statistiques sur les communes françaises sont éligibles (O > 36000), celles concernant les pays conviennent (O ~ 200  selon les sources) mais celles concernant les département français ne conviennent pas (O < 100).
- Parmi l'ensemble des données disponibles sur chacune des lignes, l'une au moins doit être **numérique** et non catégorielle. Une donnée non catégorielle posséde une relation d'ordonnancement (plus petit que, plus grand que). Exemple : la pression atmosphérique, le poids, le coût, le nombre, etc... Attention à l'utilisation de l'année comme donnée numérique, le plus souvent cette dernière est utilisée comme donnée catégorielle.
- les observations devront pouvoir être géolocalisées. Exemple : la température mesurée pour plusieurs stations météo, la taille relevée dans des zones géographiques différentes, le point de chute de météorites, etc.. Soit directement si les coordonnées géographiques sont incluses dans les observations, soit indirectement en faisant appel à une autre ressource statique (un fichier) ou dynamique (un appel à une API de géolocalisation par exemple)
- si le nombre O d'observations est très grand, les observations peuvent être sous catégorisées pour donner du sens à l'analyse. Exemple : la température mesurée pour différentes heures du jour et de la nuit, la taille relevée pour chacun des deux sexes, les dépenses de fonctionnement des villes de moins de 5000 habitants, etc...

En résumé, pour vérifier que le jeu de données choisi convient, vous devrez donc vous assurer que:

- le nombre O d'observations est suffisamment grand
- la donnée à représenter n'est pas catégorielle
- une géolocalisation est possible
    
## Représentations attendues

Il faut produire a minima un histogramme et une représentation géolocalisée:

- histogramme :  vous devez extraire les paramètres statistiques essentiels (moyenne, médiane, écart type, variance, ...)
- représentation géolocalisée : selon l'étude, les données concerneront un pays, une ville, un quartier, etc... Il faudra organiser l'affichage de façon à ce qu'il soit lisible, en particulier en limitant le nombre de données affichées si nécessaire.
