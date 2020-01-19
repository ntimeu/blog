---
title: "Hashlib - Checkez de l'intégrité !"
date: 2015-03-17T17:31:00+01:00
---

Hashlib, c'est un module Python de base de python qui vous permet de vérifier
l'intégrité de vos données via une API simple. Pour rappel, les algorithmes qui
produisent des hash prennent des données et en ressortent une "signature"
unique, qui restera la même si les données n'ont pas été changées.

{{< highlight python >}}
#!/usr/bin/env python3
# -*- coding: utf8 -*- #

import hashlib

h = hashlib.new('sha1')
h.update(b'Ma phrase que je vais vérifier')
h.hexdigest() # donne une représentation simple et lisible
h.digest() # vraie représentation, mais complexe à lire
{{< / highlight >}}


Pour en savoir plus, c'est [PAR ICI](https://docs.python.org/3/library/hashlib.html).
