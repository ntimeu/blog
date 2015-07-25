#!/usr/bin/env python3
# -*- coding: utf8 -*- #

import hmac

myhash = hmac.new(b"azerty", digestmod="sha512")
myhash.update("Ceci est un test !")
myhash.hexdigest() # donne une version lisible du hash
myhash.digest() # vrai version du hash, pas vraiment lisible
