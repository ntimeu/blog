Hashlib - Checkez de l'intégrité !
##################################

:date: 2015-03-17 17:31
:category: programmation
:tags: python, programmation, sécurité
:slug: hashlib-checkez-de-l-integrite
:author: ntimeu

Hashlib, c'est un module Python de base de python qui vous permet de vérifier
l'intégrité de vos données via une API simple. Pour rappel, les algorithmes qui
produisent des hash prennent des données et en ressortent une "signature"
unique, qui restera la même si les données n'ont pas été changées.

.. code-block:: python

    #!/usr/bin/env python3
    # -*- coding: utf8 -*- #

    import hashlib

    h = hashlib.new('sha1')
    h.update(b'Ma phrase que je vais vérifier')
    h.hexdigest() # donne une représentation simple et lisible
    h.digest() # vraie représentation, mais complexe à lire


Pour en savoir plus, c'est `PAR ICI`_.

.. _PAR ICI: https://docs.python.org/3/library/hashlib.html
