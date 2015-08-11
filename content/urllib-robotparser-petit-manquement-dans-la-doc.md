Title: urllib.robotparser - petit manquement dans la doc
Date: 2015-08-11 21:12
Categories: programmation
Tags: python, programmation
Slug: urllib-robotparser-petit-manquement-dans-la-doc
Author: ntimeu

Juste un petit bonjour, tout ça pour dire que j'ai trouvé un petit "manquement"
dans la doc de la lib python
[urllib.robotparser](https://docs.python.org/3/library/urllib.robotparser.html).

En effet, lorsque vous souhaitez respecter les fichiers
[robots.txt](http://www.robotstxt.org/) pour analyser une page web, vous êtes
censés lire ce fichier (présent à la racine du site web) et respecter les
différentes directives données par le propriétaire du site (généralement, les
directives vous demandent de ne pas analyser les parties administratives du
site, ou tout simplement vous disent

> ce n'est pas ce site que vous recherchez

## Du coup, où ce trouve ce problème ?

En fait, il n'apparaît que lorsque vous souhaitez analyser un fichier
robots.txt "à la mano", sans passer par la méthode read() de la classe
[RobotFileParser](https://docs.python.org/3/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser)
(en effet, cette méthode fait un appel direct au site, sans avoir le moindre
contrôle sur l'outil de récupération, notamment le header User-Agent de votre
requête).

L'une de solution est de n'utiliser que la classe RobotFileParser et notamment
sa méthode parse() qui a pour effet de lire le contenu du fichier de
directives. Sauf que dans la doc, le paramètre se nomme lines, et quand on n'a
pas l'habitude, lines signifie "le contenu de ton fichier" et non "une liste de
chaînes de caractères représentant le contenu du fichier ligne par ligne".

## Donc

Donc petit conseil (et un code vaut beaucoup plus qu'une langue phrase) :

{% include_code urpmdld/main.py lang:python :hidefilename: main.py %}
