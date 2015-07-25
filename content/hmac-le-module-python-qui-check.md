Title: HMAC - Le module python qui check
Date: 2015-02-17 17:09
Category: programmation
Tags: programmation, python, sécurité
Slug: hmac-le-module-python-qui-check
Author: ntimeu

Python dispose depuis plusieurs années d'un module dans sa
[librairie standard](https://docs.python.org/3/py-modindex.html) qui se nomme
[HMAC](https://docs.python.org/3/library/hmac.html). Ce module permet, en plus
de vérifier la non modification du message, de tester si c'est bien VOUS qui
avez émis ce message !


Un [HMAC](https://en.wikipedia.org/wiki/Hash-based_message_authentication_code)
est un code qui permet d'attester plusieurs propriétés sur un fichier/texte :

* il n'a pas été modifié
* il a été émis par vous


Du coup, un bon exemple pour vérifier que vous avez émis un texte est de comparer la signature que vous aviez généré à une nouvelle que vous allez générer sur ce même fichier avec la même clé. Si les deux hash concordent, c'est que le fichier n'a pas été modifié !

{% include_code hlmpqc/main.py lang:python :hidefilename: main.py %}


Pour info, la liste des hash est disponible grace au module hashlib de python, via hashlib.algorithms_available().
