#!/usr/bin/env python3
# -*- coding: utf8 -*- #

import requests

resp = requests.get("http://ntimeu.fr/links/?do=rss")
print(resp.headers)
print(resp.text)

resp = requests.post("mon API JSON", data={})
resp.json() # ici resp.json() me retourne un objet JSON que l'on pourra convertir en types python !
