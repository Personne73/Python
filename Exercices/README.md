Vous trouverez ici les exercices d'application permettant de valider les connaissances du [cours Python](https://perso.esiee.fr/~courivad/Python)


# 3. Contrôle de l'exécution d'un programme

Les nombres premiers ne sont divisibles que par 1 et eux mêmes. Ecrivez le code permettant d’afficher la vérité de " `p` est un nombre premier".

Pour rechercher (naïvement) si un nombre `p` est premier:

- POUR chaque diviseur `d` parmi les valeurs 2 et les valeurs impaires inférieures à \sqrt{p} (vérifier que ça suffit sur un exemple)
- on effectue la division entière de 𝑝 par 𝑑
- SI le reste est nul, ALORS le nombre n’est pas premier et on interrompt le parcours de la boucle en affichant False
- FIN POUR
- Sinon, il est premier et on affiche True

L’affichage doit ressembler à:

    $ python ex03.py
    731  =  17 x 43  : False
    $ python ex03.py
    733  : True
    
# Si le temps le permet

On peut définir quelques métriques pour les suites de Syracuse:

- le temps de vol : c’est le plus petit indice `k` tel que u_{k}=1. Il est de `17` pour la suite de Syracuse de source `n=15` et de `46` pour la suite de Syracuse de source `n=127`.
- le temps de vol en altitude : c’est le plus petit indice `k` tel que u_{k+1} <= u_{0} 𝑘+1≤𝑢0. Il est de `10` pour la suite de Syracuse de source `n=15` et de `23` pour la suite de Syracuse de source `n=127`
- l’altitude maximale : c’est la valeur maximale de la suite. Elle est de `160` pour la suite de Syracuse de source `n=15` et de `4372` pour la suite de Syracuse de source `n=127`.

Ecrivez le code permettant de rechercher:

- l’altitude maximale d’une suite de Syracuse et la valeur maximum de l’altitude maximale des suites de Syracuse pour `n=1` jusqu’à `n=9999`.
- le temps de vol en altitude d’une suite de Syracuse et la valeur maximum du temps de vol des suites de Syracuse pour `n=1` jusqu’à `n=9999`.
- le temps de vol en altitude d’une suite de Syracuse et la valeur maximum du temps de vol en altitude des suites de Syracuse pour `n=1` jusqu’à `n=9999`.
