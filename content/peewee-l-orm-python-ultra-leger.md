Title: Peewee - L'ORM python ultra léger
Date: 2015-04-04 19:20
Category: programmation
Tags: python, projets, bricolage
Slug: peewee-l-orm-python-ultra-leger
Author: ntimeu

Quand on travaille avec des bases de données, plusieurs problèmes apparaissent :
le moteur de base de données peut changer, les paramètres ne sont pas les mêmes
selon l'infrastrucure (en développement, en tests, en prouction ...), et
surtout il faut gérer les types des colonnes en base selon le moteur utilisé.
Un autre inconvénient, c'est que la manipuplation des données doit se faire via
le SQL, et croyez-moi, ça n'est pas forcément pratique.

Du coup, des personnes ont inventé ce que l'on appelle des
[ORM](https://en.wikipedia.org/wiki/Object-relational_mapping) (Object
Relational Mapper). Ces bibliothèques permettent de manipuler des bases de
données avec des classes. On va relier les tables d'une base de données (nom de
la colonne + type) à une classe dans le langage de programmation utilisé
(python dans notre exemple). C'est ça le mapping relationnel-object.

Donc en python, il existe plusieurs ORM, mais mon attention s'est portée sur
[Peewee](https://peewee.readthedocs.org/en/latest/), un ORM en python très
léger, et qui support les principaux SGDB libres (SQLite, MySQL, PostGreSQL).

{% include_code poul/install.sh lang:sh :hidefilename: install.sh %}

{% include_code poul/main.py lang:python :hidefilename: main.py %}

Si on enregistre le code précédent dans models.py, on peut manipuler la base de
données depuis n'importe quel code en python :

{% include_code poul/usage.py lang:python :hidefilename: usage.py %}


Donc si vous souhaitez travailler avec une base de données en python, je vous
conseille d'utiliser Peewee (et si vos besoins sont plus complexes que ce que
peut supporter Peewee, pensez à [SQLAlchemy](http://www.sqlalchemy.org/)).
