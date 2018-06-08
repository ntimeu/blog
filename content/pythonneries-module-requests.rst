Pythonneries - module Requests
##############################

:date: 2015-02-17 16:00
:category: programmation
:tags: programmation, python, projets, chroneek
:slug: pythonneries-module-requests
:author: ntimeu

Suite à l'article de `Sam et Max`_ sur le don qu'ils ont fait au créateur du
module Requests, je me suis intéressé à ce dernier, et je dois dire que le
résultat est bluffant.

Requests_ est un module assez sympathique qui permet d'effectuer des requêtes
HTTP(S) vers des sites web.

L'avantage de ce module est qu'il est très simple d'utilisation, et permet
d'utiliser les verbes HTTP (comme PUT, POST, GET et DELETE) sans devoir écrire
des centaines de lignes de code. Contrairement au module standard de Python3
urllib_, qui est simple d'utilisation pour les requêtes basiques, mais deviens
un bazar assez compliqué à gérer dès que l'objectif est d'effectuer des
requêtes avancées.

Un petit exemple de code pour la route :

.. code-block:: python

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

    import requests

    resp = requests.get("Une page web")
    print(resp.headers)
    print(resp.text)

    resp = requests.post("mon api JSON", data={})
    resp.json() # ici resp.json() me retourne un objet JSON que l'on pourra
                # convertir en types python !

.. _Sam et Max: http://sametmax.com/le-don-du-mois-python-requests/
.. _Requests: http://docs.python-requests.org/en/latest/
.. _urllib: https://docs.python.org/3/library/urllib.html
