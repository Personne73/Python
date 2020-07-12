# L'environnement de travail

[[_TOC_]]

Ce dépôt contient les ressources additionnelles (exercices, données) qui accompagnent [le cours Python](https://perso.esiee.fr/~courivad/Python/index.html), ainsi qu'une méthodologie de développement.

Pour faciliter le développement du code informatique, il est important (entre autres) de disposer :

- d’un endroit centralisé hébergeant le travail déjà réalisé
- d’un système de versionnage permettant d’archiver différentes étapes du travail

Dans le cadre de ce cours nous utiliserons le système [git](https://fr.wikipedia.org/wiki/Git). Pour une présentation (un peu) approfondie, on peut utiliser [le tutoriel OpenClassrooms](https://openclassrooms.com/fr/courses/1233741-gerez-vos-codes-source-avec-git).

L'ESIEE a déployé un serveur GitLab et vous disposez d'un compte sur la plateforme https://git.esiee.fr/. La connexion se fait avec vos identifiants habituels.

Les machines de l'ESIEE (Windows et Linux) disposent du système [git](https://fr.wikipedia.org/wiki/Git).

## Les ressources additionnelles

Pour suivre pleinement [le cours Python](https://perso.esiee.fr/~courivad/Python/index.html), des ressources additionnelles sont requises. Il s'agit des données utilisées pour les exercices, ainsi que le squelette des exercices d’application :

- Le dossier `data` contient les données nécessaires pour faire certains exercices.
- Le dossier `exercices` contient les squelettes de fichier, lorsque vous devez en utiliser. En deux versions:
    - la version "normale" ne contient que la signature des fonctions et les doctests associés
    - la version "easy" contient des informations supplémentaires sur la structuration du problème

Ces ressources sont disponibles sur ce dépôt (https://git.esiee.fr/courivad/Python). La procédure qui suit va vous permettre de récupérer ces ressources dans votre environnement personnel.

### Forker le projet initial

Le dépôt (https://git.esiee.fr/courivad/Python) ne vous appartient pas, ce qui signifie que vous avez uniquement les droits en lecture. Vous pouvez donc uniquement le copier. C'est suffisant pour une utilisation minimale.

Vous pouvez également souhaiter avoir une utilisation plus avancée et disposer de votre propre dépôt distant (avec les droits d'écriture). Vous pourrez ainsi synchroniser votre travail local avec votre propre dépôt distant et disposer ainsi dans le cloud d'une version "à jour" de votre travail. A condition bien évidemment d'effectuer les opérations de synchronisation nécessaires (ce n'est pas automatique).

Le processus de copie d'un dépôt distant dans votre espace personnel distant s'appelle un "fork". Un fork est une copie complète du projet. Par la suite, cette copie sera appelée "repo distant". Vous pourrez ultérieurement ajouter, supprimer ou modifier du contenu de ce repo distant:

- connectez vous [au Git ESIEE](https://git.esiee.fr/) avec vos identifiants personnels
- rechercher le projet https://git.esiee.fr/courivad/Python
- le forker (vous trouverez la commande quelque part sur la page du projet)

Une fois cette étape effectuée, vous dsposez de la totalité des ressources nécessaires dans votre espace Git personnel (cloud).

### Cloner le projet sur une machine locale

Le travail de développement s'effectue sur une machine locale (votre machine personnelle ou une machine de l'ESIEE). Il faut donc copier le repo distant sur la machine de développement. C'est le processus de clonage.

Sur une machine locale, on clone le projet à partir du repo distant avant de poursuivre le travail de développement. Cloner un projet c'est créer un répertoire local contenant la totalité des fichiers du repo distant. 


#### Windows

Lancez la commande `Git Bash`, qui ouvre un terminal configuré pour fonctionner avec `git`.
 
- placez vous dans votre répertoire de travail. Sur une machine de l'ESIEE, placez vous dans votre espace réseau (disque U:) : `cd /u`
- clonez votre repo distant : `git clone https://git.esiee.fr/<YOUR_GIT_NAME>/Python`

#### Linux

Le terminal standard est configuré pour fonctionner directement avec `git`.

- placez vous dans votre répertoire de travail. Sur une machine de l'ESIEE, vous vous trouvez automatiquement dans votre espace réseau
- clonez votre repo distant : `git clone https://git.esiee.fr/<YOUR_GIT_NAME>/Python`



## Méthodologie de développement

Le travail de développement se fait sur une machine locale (dans le répertoire `Python` créé lors de l'opération de clonage) avec un terminal et un éditeur de texte ([Visual Studio Code](https://code.visualstudio.com/download)). Suivant le système d'exploitation utilisé, il faudra démarrer un terminal spécifique (Windows) ou non (Linux).

### Interpréteur Python

Python dispose d'un interpréteur de type REPL permettant d'exécuter rapidement quelques instructions simples.

#### Windows

Nous travaillons dans l'environnement Anaconda. Il est installé sur les machines Windows de l'ESIEE et disponible au téléchargement [ici](https://www.anaconda.com/download/) pour vos machines personnelles.

Pour disposer de l'ensemble de l'environnement Anaconda, **il faut démarrer un terminal Anaconda Prompt** (menu "Démarrer" de Windows). Toutes les commandes Windows sont disponibles. Attention, un terminal classique (`cmd`) ne dispose pas de toutes les variables d'environnement nécessaires pour permettre l'utilisation de l'environnement Anaconda.

Dans ce terminal, l'interpréteur Python 3.7 se lance avec la commande `python`:

    $ python --version
    Python 3.7.x
    

#### Linux

Le terminal classique convient. L'interpréteur Python 3.7 se lance directement avec la commande `python3`:

    $ python3 --version
    Python 3.7.x
    
Attention la commande `python` lance une version obsolète de Python
    
    $ python --version
    Python 2.7.x
    

### Coder

Lorsqu'on développe des programmes plus complexes, il est nécessaire de stocker les instructions à exécuter dans un fichier avec un éditeur de texte.

Quel que soit l'OS choisi (Windows ou Linux), Le travail peut s'effectuer entièrement dans l'environnement [Visual Studio Code](https://code.visualstudio.com/download).

#### Windows

L'éditeur de texte [Visual Studio Code](https://code.visualstudio.com/download) est démarré depuis le terminal Anaconda avec la commande `code`.

    $ code
    $
    
#### Linux

L'éditeur de texte [Visual Studio Code](https://code.visualstudio.com/download) est démarré depuis le bureau Linux.


### L'éditeur de texte

[Visual Studio Code](https://code.visualstudio.com/download) propose une interface intégrée comprenant:

- l'éditeur de texte proprement dit
- un navigateur de fichier
- un terminal intégré
- et d'autres fonctionnalités facilitant la programmation


#### Ouvrir le répertoire de travail

Ouvrir le dossier `Python` qui contient les ressources nécessaires pour ce cours avec la commande `Open Folder...`. Au démarrage, ce répertoire est un clone de votre repo distant (https://git.esiee.fr/<YOUR_GIT_NAME>/Python). Il contiendra par la suite le travail réalisé dans le cadre de ce cours. 

Vous pouvez utiliser `git`, depuis le terminal ou depuis Visual Studio Code, pour maintenir la synchronisation entre votre répertoire local et votre repo distant.

![Ouvrir le répertoire de travail](_images/openfolder.png)

#### Le terminal intégré

Visual Studio Code dispose d'un terminal intégré, que l'on fait apparaître ou disparaître dans le menu Afficher.

![Ouvrir le répertoire de travail](_images/afficher-terminal.png)

Ce terminal est une vue intégrée du terminal Linux ou Windows (`Anaconda Prompt`.) 

![Terminal intégré](_images/terminal.png)

Ce terminal intégré permet :

- d'exécuter les programmes Python avec la syntaxe `python nom_du_programme.py` (Windows) ou `python3 nom_du_programme.py` (Linux).
- de lancer l'interpréteur interactif avec la syntaxe `python` (Windows) ou `python3` (Linux) . Le prompt (l'invite de commande) de ce dernier est différent (`>>>`) et permet d'identifier la nature des commandes attendues. 
  
Une erreur courante est d'entrer des commandes Python dans un terminal (Windows ou Linux) ou l'inverse, des commandes Windows ou Linux dans un interpréteur Python.

![Python](_images/python.png)

### Synchroniser son travail avec le repo distant

Tout au long du cours vous pouvez être amenés à utiliser plusieurs machines de développement (des machines différentes dans les salles de l’ESIEE, votre machine personnelle, etc...). Si vous maintenez la synchronisation entre repo distant et repo local, vous pourrez disposer à tout moment de la dernière version de votre travail.

#### Au début de la séance

Au début de chaque nouvelle séance, on récupére les modifications depuis le repo distant : `git pull`

#### A la fin de la séance

A la fin de chaque nouvelle séance:

- on ajoute les fichiers du répertoire à l'index : `git add .`
- on enregistre les modifications dans le repo local : `git commit -m "Travail effectué lors de la première séance"`. L'idée générale est de faire un commit à chaque étape logique du travail. Par exemple à la fin de chaque séance de TP...
- on pousse les modifications de la machine locale vers le repo distant : `git push origin master`


### Environnement virtuel

Dans un environnement complexe, où des conflits de versions de packages peuvent apparaître, il est possible de mettre en oeuvre le concept d'environnement virtuel. On utilisera alors de préférence [pipenv](https://github.com/pypa/pipenv) qui permet de créer des environnements isolés et reproductibles.

### Ajouter des packages

Il sera parfois nécessaire d'installer des modules additionnels. La procédure est assez similaire quel que soit le système d'exploitation et utilisera l'utilitaire `pip <https://pip.pypa.io/en/stable/>`_, l'installateur de package de Python.

#### Windows

Bien que l'environnement Anaconda soit assez complet, on peut installer des packages additionnels depuis le terminal `Anaconda Prompt`:

    $ pip install un_package
    Collecting un_package
    [...]
    Successfully installed [...]

Si l'installation s'est correctement déroulée, l'importation du module doit être possible:

    $ python
    Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import un_package
    >>> 

#### Linux

Sous Linux, l'utilitaire `pip3` est utilisé:

    $ pip3 install un_package
    Collecting un_package
    [...]
    Successfully installed [...]






