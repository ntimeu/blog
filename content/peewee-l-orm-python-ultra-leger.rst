Peewee - L'ORM python ultra léger
#################################

:date: 2015-04-04 19:20
:category: programmation
:tags: python, projets, bricolage
:slug: peewee-l-orm-python-ultra-leger
:author: ntimeu

Quand on travaille avec des bases de données, plusieurs problèmes apparaissent :
le moteur de base de données peut changer, les paramètres ne sont pas les mêmes
selon l'infrastrucure (en développement, en tests, en prouction ...), et
surtout il faut gérer les types des colonnes en base selon le moteur utilisé.
Un autre inconvénient, c'est que la manipuplation des données doit se faire via
le SQL, et croyez-moi, ça n'est pas forcément pratique.

Du coup, des personnes ont inventé ce que l'on appelle des ORM_ (Object
Relational Mapper). Ces bibliothèques permettent de manipuler des bases de
données avec des classes. On va relier les tables d'une base de données (nom de
la colonne + type) à une classe dans le langage de programmation utilisé
(python dans notre exemple). C'est ça le mapping relationnel-object.

Donc en python, il existe plusieurs ORM, mais mon attention s'est portée sur
Peewee_, un ORM en python très léger, et qui supporte les principaux SGDB libres
(SQLite, MySQL, PostGreSQL).

.. code-block:: bash

    pip install peewee


.. code-block:: python

    #!/usr/bin/env python3
    # -*- coding: utf8 -*-

    import peewee

    db = peewee.SqliteDatabase("~/test.db")

    class User(peewee.Mode):
        name = peewee.CharField(max_length=255, unique=True)
        inscription = peewee.DateTimeField(default=datetime.datetime.now)

        class Meta:
            database = db


Si on enregistre le code précédent dans models.py, on peut manipuler la base de
données depuis n'importe quel code en python :

.. code-block:: python

    #!/usr/bin/env python3
    # -*- coding: utf8 -*- #

    import models

    models.db.connect()

    # le code suivant enregistre un nouvel utilisateur dans la base
    usr = models.User.create(name="Thomas")

    # on peut également modifier l'utilisateur, et le mettre à jour en base
    usr.name="Jean"
    usr.save()


Donc si vous souhaitez travailler avec une base de données en python, je vous
conseille d'utiliser Peewee (et si vos besoins sont plus complexes que ce que
peut supporter Peewee, pensez à SQLAlchemy_).

.. _ORM: https://en.wikipedia.org/wiki/Object-relational_mapping
.. _Peewee: https://peewee.readthedocs.org/en/latest/
.. _SQLAlchemy: http://www.sqlalchemy.org/
