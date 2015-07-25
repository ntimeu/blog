#!/usr/bin/env python3
# -*- coding: utf8 -*-

import peewee

db = peewee.SqliteDatabase("~/test.db")

class User(peewee.Mode):
    name = peewee.CharField(max_length=255, unique=True)
    inscription = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
