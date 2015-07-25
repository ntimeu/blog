Title: Python - je n'y crois toujours pas
Date: 2015-07-02 19:09
Categories: programmation
Tags: python, programmation, projets
Slug: python-je-n-y-crois-toujours-pas
Author: ntimeu

Depuis ce matin, je réalise un petit projet en python (3, parce que c'est le
bien) et je dois parser des URIs. Donc j'utilise la fonction urlparse du module
[urllib.parse](https://docs.python.org/3/library/urllib.parse.html) quand tout
à coup, je me pose la question : "et si l'URI contient une adresse IP ?" (v4 ou
v6).

### Parce que dans ce cas, il faut vérifier que l'IP ne soit pas locale !

Et là, les difficultées apparaissent, il faut parser des IPs, savoir si elles
sont en v4 ou v6, etc ... Et là, je tombe sur le module Python
[ipaddress](https://docs.python.org/3/library/ipaddress.html), qui fait tout ça
pour nous ! A chaque fois que je reprends Python, je tombe sur de nouvelles
fonctionnalités toujours plus pratiques, et surtout intégrées par défaut !
Franchement, merci aux développeurs de Python !
