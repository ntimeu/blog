#!/usr/bin/env python3
# -*- coding: utf8 -*- #

import hashlib

h = hashlib.new('sha1')
h.update(b'Ma phrase que je vais vérifier')
h.hexdigest() # donne une représentation simple et lisible
h.digest() # vraie représentation, mais complexe à lire
