---
title: "HMAC - Le module python qui check"
date: 2015-02-17T17:09:00+01:00
---

Python dispose depuis plusieurs années d'un module dans sa
[librairie standard](https://docs.python.org/3/py-modindex.html)
qui se [nomme HMAC](https://docs.python.org/3/library/hmac.html). Ce module
permet, en plus de vérifier la non modification du message, de tester si c'est
bien VOUS qui avez émis ce message !


Un [hmac](https://en.wikipedia.org/wiki/Hash-based_message_authentication_code)
est un code qui permet d'attester plusieurs propriétés sur un fichier :

* il n'a pas été modifié
* il a été émis par vous


Du coup, un bon exemple pour vérifier que vous avez émis un texte est de
comparer la signature que vous aviez généré à une nouvelle que vous allez
générer sur ce même fichier avec la même clé. Si les deux hash concordent,
c'est que le fichier n'a pas été modifié !

{{< highlight python >}}
#!/usr/bin/env python3
# -*- coding: utf8 -*- #

import hmac

myhash = hmac.new(b"azerty", digestmod="sha512")
myhash.update("Ceci est un test !")
myhash.hexdigest() # donne une version lisible du hash
myhash.digest() # vrai version du hash, pas vraiment lisible
{{< / highlight >}}


Pour info, la liste des hash est disponible grace au module hashlib de python,
via hashlib.algorithms_available().
