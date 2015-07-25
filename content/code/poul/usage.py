#!/usr/bin/env python3
# -*- coding: utf8 -*- #

import models

models.db.connect()

# le code suivant enregistre un nouvel utilisateur dans la base
usr = models.User.create(name="Thomas")

# on peut également modifier l'utilisateur, et le mettre à jour en base
usr.name="Jean"
usr.save()
