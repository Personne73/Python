Vous trouverez ici les exercices d'application permettant de valider les connaissances du [cours Python](https://perso.esiee.fr/~courivad/Python)


# 3. Contrôle de l'exécution d'un programme

L'exercice d'application ci dessous correspond au chapitre [Contrôle de l’exécution d’un programme](https://perso.esiee.fr/~courivad/Python/03-controle.html).

Les nombres premiers ne sont divisibles que par 1 et eux mêmes. Ecrivez le code permettant d’afficher la vérité de " `p` est un nombre premier ".

Pour rechercher (naïvement) si un nombre `p` est premier:

- POUR chaque diviseur `d` parmi les valeurs `2` et les valeurs impaires inférieures à $`\sqrt{p}`$ (vérifier que ça suffit sur un exemple)
    - on effectue la division entière de `p` par `d`
    - SI le reste est nul, ALORS le nombre n’est pas premier et on interrompt le parcours de la boucle en affichant False
- FIN POUR
- Sinon, il est premier et on affiche True

L’affichage doit ressembler à:

    $ python ex03.py
    731  =  17 x 43  : False
    $ python ex03.py
    733  : True
    
## Si le temps le permet

On peut définir quelques métriques pour les suites de Syracuse:

- le temps de vol : c’est le plus petit indice `k` tel que $`u_{k}=1`$. Il est de `17` pour la suite de Syracuse de source `n = 15` et de `46` pour la suite de Syracuse de source `n = 127`.
- le temps de vol en altitude : c’est le plus petit indice `k` tel que $`u_{k+1} <= u_{0}`$. Il est de `10` pour la suite de Syracuse de source `n = 15` et de `23` pour la suite de Syracuse de source `n = 127`
- l’altitude maximale : c’est la valeur maximale de la suite. Elle est de `160` pour la suite de Syracuse de source `n = 15` et de `4372` pour la suite de Syracuse de source `n = 127`.

Ecrivez le code permettant de rechercher:

- l’altitude maximale d’une suite de Syracuse et la valeur maximum de l’altitude maximale des suites de Syracuse pour `n = 1` jusqu’à `n = 9999`.
- le temps de vol en altitude d’une suite de Syracuse et la valeur maximum du temps de vol des suites de Syracuse pour `n = 1` jusqu’à `n = 9999`.
- le temps de vol en altitude d’une suite de Syracuse et la valeur maximum du temps de vol en altitude des suites de Syracuse pour `n = 1` jusqu’à `n = 9999`.

# Fonctions et modules

L'exercice d'application ci dessous correspond au chapitre [Fonctions et modules](https://perso.esiee.fr/~courivad/Python/04-fonctions.html).

Encapsuler dans une fonction booléenne `est_premier()` le code correspondant à l’exercice d’application du chapitre [Contrôle de l’exécution d’un programme](https://perso.esiee.fr/~courivad/Python/03-controle.html). Ajouter une docstring et des doctest. Vérifier que les tests passent et que la fonction `help()` donne bien le résultat attendu.

Utiliser la fonction `est_premier()` pour rechercher les `n` premiers nombres premiers.

## Si le temps le permet

Utiliser la fonction `est_premier()` pour rechercher:

- le premier nombre de Fermat $`2^{2^n+1}`$ qui n’est pas premier.
- le premier nombre premier après un entier `n` donné. Quel est le premier nombre premier après `n = 100000` ?
- le premier couple de nombres premiers jumeaux après un entier `n` donné (`p` et `p'` sont des nombres premiers jumeaux si `p` et `p'` sont premiers et si `p'-p = 2`). Quel est le premier couple de nombres premiers jumeaux après `n = 100000` ?
- le premier nombre premier de Germain après un entier `n` donné (un entier `p` est un nombre premier de Germain si `p` et `2p+1` sont premiers). Quel est le premier nombre premier de Germain après `n = 100000` ?


# Les chaines de caractères

Les exercices d'application ci dessous correspondent au chapitre [Chaines de caractères](https://perso.esiee.fr/~courivad/Python/05-chaines.html).

Un palindrome est un mot ou une phrase qui se lit indifféremment de droite à gauche et de gauche à droite. Ecrire une fonction `pal()` permettant d’effectuer ce test (les espaces seront ignorés et minuscule et majuscules seront considérées comme identiques).

Pour cet exercice, vous devez utiliser en priorité le squelette contenu dans le fichier `ex05.py`. En cas de difficulté, le fichier `ex05-easy.py` contient des renseignements supplémentaires. 

Vous devez écrire le code de la fonction `pal()` en utilisant éventuellement des `print()` intermédiaires pour observer les valeurs des variables au cours de l’exécution. Ces `print()` devront être retirés lorsque la fonction sera correcte.

A chaque modification de `pal()`, tester son fonctionnement dans la fonction `main()` en appelant `pal()` pour un argument particulier et en affichant la valeur de retour. Jeter un oeil aux doctests de la fonction pour avoir un exemple d’appel et d’utilisation de la valeur de retour.

Une fois la fonction `pal()` opérationnelle pour un argument, ET SEULEMENT DANS CE CAS, lancer les doctests avec la commande suivante, exécutée dans un terminal:

- Windows : `python -m doctest ex05.py -v`
- Linux : `python3 -m doctest ex05.py -v`

Une version plus élaborée pourrait traiter le cas des caractères accentués et de la ponctuation.

## Si le temps le permet

Ecrire la fonction `check_password()` permettant de tester la robustesse d’un mot de passe. Le mot de passe est considéré comme fort si:

- sa longueur est supérieure ou égale à 10 symboles
- il a au moins un chiffre
- il contient au moins une lettre majuscule et une lettre minuscule.

Le mot de passe contient uniquement des lettres latines ASCII ou des chiffres. Une version plus élaborée pourrait imposer la présence d’un signe de ponctuation.


# Les listes

Les exercices d'application ci dessous correspondent au chapitre [Les listes](https://perso.esiee.fr/~courivad/Python/06-listes.html).

Pour ces exercices, vous devez utiliser en priorité le squelette contenu dans le fichier `ex06.py`. En cas de difficulté, le fichier `ex06-easy.py` contient des renseignements supplémentaires.

## Contenu d’un répertoire

Utiliser les modules `os` et `os.path` pour écrire une fonction `scand()` qui prend en argument un nom de répertoire et retourne deux listes de strings :

- l’une contient le nom des fichiers du répertoire passé en argument
- l’autre le nom des répertoires.

Vous devez écrire le code de la fonction `scand()` en utilisant éventuellement des `print()` intermédiaires pour observer les valeurs des variables au cours de l’exécution. Ces `print()` devront être retirés lorsque la fonction sera correcte. On s’interessera plus particulièrement aux fonctions `listdir()`, `isfile()`, `isdir()`, et `join()`. Utiliser les “list comprehension” pour une écriture synthétique.

A chaque modification de `scand()`, tester son fonctionnement dans la fonction `main()` en appelant `scand()` pour un argument particulier et en affichant la valeur de retour. Jeter un oeil aux doctests de la fonction pour avoir un exemple d’appel et d’utilisation de la valeur de retour.

Une fois la fonction `scand()` opérationnelle pour un argument, ET SEULEMENT DANS CE CAS, lancer les doctests avec la commande suivante:

- Windows : `python -m doctest ex06.py -v`
- Linux : `python3 -m doctest ex06.py -v`

## Liste des extensions

Ecrire une fonction `searchext()` qui prend en argument une liste de strings contenant des noms de fichiers (du type de celles renvoyées par `scand()`) et retourne la liste des extensions de ces fichiers. Les extensions peuvent apparaître plusieurs fois dans la liste retournée, et doivent être en minuscules.

## Recherche de langue

Ecrire une fonction `guess_language()` qui prend en argument une string contenant un texte dans une langue (anglais, français, allemand et espagnol) et retourne la langue utilisée sous forme de chaîne de caractères. La détection se base sur l’analyse fréquentielle. La liste des fréquences est fournie dans les variables globales ENGLISH, FRENCH, GERMAN et SPANISH. TRTAB est utilisée dans la méthode `translate()` qui permet de remplacer les caractères accentués par les caractères non accentués correspondant dans la chaîne de caractères sur laquelle elle est appelée.

Pour tester le bon fonctionnement, les chaînes de caractères LCELR, IF, POEMAXX et GOETHE contiennent des textes dans chacune des langues considérées.

## Si le temps le permet

### Nombre de Harshad

En mathématiques récréatives, un nombre Harshad est un entier naturel qui est divisible par la somme de ses chiffres dans une base donnée. Ecrire la fonction `is_harshad()` permettant de vérifier si un entier `n` (base 10) passé en paramètre est un nombre de Harshad ou pas. La fonction doit retourner un booléen. Vous écrirez également les doctests associés. Afficher les nombres de Harshad jusqu’à 100.

### Nombre heureux

Un entier naturel est un nombre heureux si, lorsqu’on calcule la somme des carrés de ses chiffres dans son écriture en base 10 puis la somme des carrés des chiffres du nombre obtenu et ainsi de suite, on aboutit au nombre 1. Ecrire la fonction récursive `is_happy()` permettant de vérifier si un entier `n` passé en paramètre est un nombre heureux ou pas. La fonction doit retourner un booléen. Vous écrirez également les doctests associés. Afficher les nombres heureux jusqu’à 100.


# Les tuples

Les exercices d'application ci dessous correspondent au chapitre [Les tuples](https://perso.esiee.fr/~courivad/Python/07-tuples.html).

Ecrire la fonction `artcode()` qui prend une chaîne de caractères pour argument, et retourne une liste de tuples. Chaque tuple est composé d’un caractère (et d’un seul) et du nombre d’occurences consécutives de ce caractère. Par exemple, la chaîne `"MMMMaaacXolloMM"` est représentée par la liste `[('M', 4), ('a', 3), ('c', 1), ('X', 1), ('o', 1), ('l', 2), ('o', 1), ('M', 2)]`.

Ecrire la fonction réciproque `artdecode()` qui prend une liste de tuples en argument et retourne la chaîne de caractères correspondante. Cette fonction est la fonction réciproque de `artcode()`.

Construire les chaînes de caractères correspondant aux variables L1 et L2. Vous pouvez trouver des [ASCII art](https://en.wikipedia.org/wiki/ASCII_art) simples sur le site [ASCII art archive](https://www.asciiart.eu/) ou construire les votres à partir d’images et de [ce générateur](https://www.ascii-art-generator.org/).

Lancement des tests:

- Windows : `python -m doctest ex07.py -v`
- Linux : `python3 -m doctest ex07.py -v`


# Les sets

L'exercice d'application ci dessous correspond au chapitre [Les sets](https://perso.esiee.fr/~courivad/Python/08-sets.html).

Modifier la seule instruction return de la fonction `searchext()` de l’exercice d’application sur les listes pour que la liste des extensions retournée ne contienne chaque extension qu'une et une seule fois.


# Les fichiers

L'exercice d'application ci dessous correspond au chapitre [Les fichiers](https://perso.esiee.fr/~courivad/Python/09-files.html).

Ecrire la fonction `extract_temp()` qui prend en argument une date au format `AAAAMMJJ`, un code de station météo parmi ceux disponibles dans la liste des stations météo (`Data/stations-meteo.csv`) et retourne une liste des températures.

Pour cet exercice, vous devez utiliser en priorité le squelette contenu dans le fichier `ex09.py`. En cas de difficulté, le fichier `ex09-easy.py` contient des renseignements supplémentaires. 

Vous devez écrire le code de la fonction `extract_temp()` en utilisant éventuellement des `print()` intermédiaires pour observer les valeurs des variables au cours de l’exécution. Ces `print()` devront être retirés lorsque la fonction sera correcte.

A chaque modification de `extract_temp()`, tester son fonctionnement dans la fonction `main()` en appelant `extract_temp()` pour un argument particulier et en affichant la valeur de retour.

Une fois la fonction `extract_temp()` opérationnelle pour un argument, ET SEULEMENT DANS CE CAS, lancer les doctests :

- Windows : `python -m doctest ex07.py -v`
- Linux : `python3 -m doctest ex07.py -v`

Quelques indications:

- le fichier `Data/meteofrance2014.zip` contient les observations météorologiques en France pour l’année 2014, et l’explication des variables se trouve [sur ce lien](https://donneespubliques.meteofrance.fr/client/document/doc_parametres_synop_168.pdf).
- le module `zipfile` permet la manipulation des fichiers compressés. En particulier la méthode `namelist()` permet de lister le contenu de l’archive.
- lorsqu’on travaille avec une archive, la fonction `csv.reader()` n’est pas disponible. Il faut utiliser la méthode `read()` qui retourne une séquence de bytes.
- cette séquence de bytes est convertie en `str` avec la méthode `decode()`.

---
*Note* : La liste ne permet pas une performance algorithmique optimale. La structure de données la plus appropriée à ce type de problème est le dictionnaire que nous verrons au chapitre suivant.
---


